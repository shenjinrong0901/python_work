#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "util.h"
#include <float.h>
#include <assert.h>
#include <unistd.h>
#include "extract.h"
#include "getmask.h"
#include "getqual.h"
#include "file.h"
#include "definitions.h"
#include "grad.h"
#include "pi.h"
#include "linkedlist.h"
#include <time.h>
#include <iostream>
using namespace std;



/*
 *   Uniform random generator
 */
int uniform(int rangeLow, int rangeHigh)
{
    int myRand = (int)rand();
    int range = rangeHigh - rangeLow + 1; //+1 makes it [rangeLow, rangeHigh], inclusive.
    int myRand_scaled = (myRand % range) + rangeLow;
    return myRand_scaled;
}



/*
 *    Find the minimum and maximum values of a vector.
 */
void find_min_max(float *map, int length,
                  float *min_val, float *max_val,
                  int *index_min, int *index_max)
{
    int k, imin, imax;
    float min_=FLT_MAX, max_=FLT_MIN;
    
    for (k=0; k<length; k++) {
        if (map[k]<min_) {
            min_ = map[k];
            imin = k;
        }
        if (map[k]>max_) {
            max_ = map[k];
            imax = k;
        }
    }
    
    *min_val = min_;
    *max_val = max_;
    *index_min  = imin;
    *index_max  = imax;
}




/*
 *   Compute histogram mapping from quality to bin interval in the partition
 */
int *hist_mapping(const char *fname, float *qual_map, int xsize, int ysize,
                  float min_val, float max_val,
                  int L, int n, int flag_debug, int *intervals)
{
    int   *hist, *map, *h0, *h1, *h2;
    int   dim, len, lm, max, k, bin, c, j, g;
    int   index_min, index_max, inc, flag, l, index, r;
    float width;
    double p, x;
    char  prefix[120];
    FILE  *ofh;
    nodeList *tmp;
    
    dim  = xsize*ysize;
    len  = n*L;
    max  = dim / L;
    
    printf("Maximum %d\n", max);
    
    
    /* histogram variables */
    
    nodeList **list;
    nodeList *list_nodes;
    
    
    assert(list = (nodeList **)malloc(sizeof(nodeList *)*len));
    
    for (k=0; k<len; k++)
        list[k] = NULL;
    
    // shared memory
    
    assert(list_nodes = (nodeList *)malloc(sizeof(nodeList)*dim));
    
    
    // Allocate memory
    
    AllocateInt(&hist, len, "histogram");
    AllocateInt(&h0, len, "histogram");
    AllocateInt(&h1, len, "histogram");
    AllocateInt(&h2, max+1, "histogram");
    AllocateInt(&map, dim, "mapping");
    

    
    
    // Compute histogram with n*L bins
    
    width = (max_val - min_val) / (float)len;
    
    for (k=0; k<dim; k++)
    {
        bin = (int)floor((qual_map[k] - min_val) / width);
        if (bin > len-1) bin = len-1;
        if (bin<0) bin = 0;
        hist[bin]++;
        insertIni(k, &list[bin], list_nodes);
    }
    
    // save initial histogram
    
    if (flag_debug) {
        printf("Saving initial histogram of length %d\n",len);
        strcpy(prefix, "data/");
        strcat(prefix, fname);
        strcat(prefix, "_dist_0.hist");
        OpenFile(&ofh, prefix, "w");
        WriteInt(ofh, hist, len, "Initial histogram");
    }
    
    
    // merge histogram
    
    k = 0; c = 0; j = 0; g = 0;
    
    while (k<len)
    {
        if (c<=max) {
            c+=hist[k];
            g++;
            k++;
        }
        else {
            h0[j] = c;
            h1[j] = g;
            c = 0;
            g = 0;
            j++;
        }
    }
    
    if (c>0 && j<len) {
        h0[j] = c;
        h1[j] = g;
        j++;
    }
    
    lm = j;
    
    /*
    printf("Maximum %d\n",max);
    for (k=0; k<lm; k++)
    {
        inc = (int)round((float)h0[k] / (float)max);
        printf("%d\t%d\t%d\t%d\n", k, h0[k], h1[k], inc);
    }
     */
    
    
    // save merged histogram
    
    if (flag_debug) {
        printf("Saving merged histogram of length %d\n",lm);
        strcpy(prefix, "data/");
        strcat(prefix, fname);
        strcat(prefix, "_dist_1.hist");
        OpenFile(&ofh, prefix, "w");
        WriteInt(ofh, h0, lm, "Initial histogram");
    }
    
    // compute mapping

    index_min = 0;
    k = 0;
    l = 0;
    
    while (k<lm)
    {
        inc = (int)round((float)h0[k] / (float)max);
        index_max = h1[k];
        if (inc==0 && index_max>0) inc=1;
     
        for (g=index_min; g<(index_min+index_max); g++)
        {
            for (tmp = list[g]; tmp!=NULL; tmp=tmp->sig) // explore each bin
            {
                index = tmp->index;
                
                if (inc==1) {
                    map[index] = l;
                    h2[l]++;
                }
                else {
                    r = l + uniform(0,inc-1);
                    map[index] = r;
                    h2[r]++;
                }
            }
        
        }
        
        index_min+=index_max;
        l+=inc;
        k++;
    }
    
    *intervals = l;

    
    // save final histogram
    
    if (flag_debug) {
        printf("Saving final histogram of length %d\n",l);
        strcpy(prefix, "data/");
        strcat(prefix, fname);
        strcat(prefix, "_dist_2.hist");
        OpenFile(&ofh, prefix, "w");
        WriteInt(ofh, h2, l, "Final histogram");
    }
    

    
    // release memory
    
    free(hist);
    free(h0);
    free(h1);
    free(h2);
    free(list);
    free(list_nodes);
 

    
    return map;
}




/*
 *    Quality guide phase unwrapping algorithm
 */
double Quality_guide_phase_unwrapping(const char *data_path,
                                      const char *pname,
                                   int xsize,
                                   int ysize,
                                   int num_levels,
                                   int N,
                                   int flag_mask,
                                   int flag_qual,
                                   int int_qual_flag,
                                   float int_max_qual)
{
    /* data variables */
    
    int           *path, *mapping;
    float         *phase, *qual_map, *soln, *mask;
    unsigned char *unwrap;
    
    
    /* other variables */

    FILE          *ifp, *ofp, *ifq, *ifm;
    char          prefix[120], fname[120];
    double        elapsed_time;
    float         grad, minval, maxval, high_qual, valf, aux;
    int           k, length, index, p, q, iter=0, bin, l;
    int           a, b, w, x, y, intervals;
    int           imin, imax, binarg, total=0, maxbin, resumed, flag;
    int           flag_debug = 0;


    struct timespec total_start, total_end;

    
	/* adjoin-list variables */
    
    nodeList **adjoin_list;
    nodeList *list_nodes;
    nodeList **list_last;
    
    
    
    /* * * * * * * * * * * * * * * * * * * * * * * *
     *                                             *
     *             ALLOCATE MEMORY                 *
     *                                             *
     * * * * * * * * * * * * * * * * * * * * * * * */
    
    length = xsize*ysize;
    
    AllocateFloat(&phase, length, "phase data");
    AllocateFloat(&qual_map, length, "quality data");
    AllocateFloat(&soln, length, "solution array");
    AllocateByte(&unwrap, length, "flag array");
    AllocateInt(&path, length, "integration path");
    AllocateFloat(&mask, length, "solution array");

    

    
    
    /* * * * * * * * * * * * * * * * * * * * * * * *
     *                                             *
     *      READ DATA: PHASE AND QUALITY MAP       *
     *                                             *
     * * * * * * * * * * * * * * * * * * * * * * * */
    
    
    // load phase
    strcpy(prefix, data_path);
    strcat(prefix,"/data/");
    strcat(prefix,pname);
    strcpy(fname,prefix);
    strcat(fname, ".phase");
    
    OpenFile(&ifp, fname, "r");
    GetPhase(3, ifp, fname, phase, xsize, ysize);
    
    // normalize phase
    
    find_min_max(phase, length, &minval, &maxval, &imin, &imax);
    printf("Min&Max phase: %f %f\n",minval, maxval);
    
    for (k=0; k<length; k++)
        phase[k] = (phase[k] - minval)/(maxval-minval);


    
    
    // load mask
    
    if (flag_mask)
    {
        strcpy(prefix, data_path);
        strcat(prefix,"/data/");
        strcat(prefix,pname);
        strcpy(fname,prefix);
        strcat(fname, ".mask");
        OpenFile(&ifm, fname, "r");
        GetPhase(3, ifm, fname, mask, xsize, ysize);
    }
    else
    {
        for (k=0; k<length; k++)
          mask[k] = 1;
    }




    
    // load quality map and normalize data
    
    if (flag_qual)
    {
        strcpy(prefix, data_path);
        strcat(prefix,"/data/");
        strcat(prefix,pname);
        strcpy(fname,prefix);
        strcat(fname, ".qual");
        OpenFile(&ifq, fname, "r");
        GetPhase(3, ifq, fname, qual_map, xsize, ysize);
    }
    
    
    
    find_min_max(qual_map, length, &minval, &maxval, &imin, &imax);
    printf("\nMin. qual. val. %f\n", minval);
    printf("Max. qual. val. %f\n", maxval);
    
    
    for (k=0; k<length; k++) {
        qual_map[k] = (qual_map[k] - minval)/(maxval-minval);
        
        if (int_qual_flag)
            qual_map[k] = floorf(int_max_qual*qual_map[k]);
    }
    
    minval = 0;
    
    if (int_qual_flag)
        maxval = int_max_qual;
    else
        maxval = 1;
    
    
    

    

    
    
    /* * * * * * * * * * * * * * * * * * * * * * * * *
     *                                               *
     *               COMPUTE MAPPING                 *
     *                                               *
     * * * * * * * * * * * * * * * * * * * * * * * * */
    

    
    srand(time(NULL));

    
    mapping = hist_mapping(pname, qual_map, xsize, ysize, minval, maxval,
                           num_levels, N, flag_debug, &intervals);
    

    
    
    
    // Allocate memory for the adjoin-list
    
    adjoin_list = (nodeList **)malloc(sizeof(nodeList *)*intervals);
    list_last = (nodeList **)malloc(sizeof(nodeList *)*intervals);
    
    for (k=0; k<intervals; k++) {
        adjoin_list[k] = NULL;
        list_last[k] = NULL;
    }
    
    // shared memory
    
    list_nodes = (nodeList *)malloc(sizeof(nodeList)*length);
    
    
    
    /* * * * * * * * * * * * * * * * * * * * * * * *
     *                                             *
     *     QUALITY-GUIDE UNWRAPPING ALGORITHM      *
     *                                             *
     * * * * * * * * * * * * * * * * * * * * * * * */
    
    
    

    
    // Step 1. Find starting point (highest quality value).
    
    high_qual = maxval;
    index = imax;
    
    printf("\nStarting point: y=%d x=%d qual=%f index=%d\n", index/xsize, index%xsize, high_qual, index);
    
    
    // Step 2. Store its phase value in the solution array soln.
    
    soln[index] = phase[index];
    
    
    // Steo 2.1 save path integration
    
    path[index] = iter++;
    
    

    // Step 3. Mark as unwrapped.
    
    unwrap[index] = 1;
    
    

    // Step 4. Insert in the list.
    
    bin = mapping[index];
    insertIni(index, high_qual, &adjoin_list[bin], &list_last[bin], list_nodes);
    total++;
    
    
    
    // previous bin interval
    
    resumed = bin;

    // ** starting time
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &total_start);

    
    // unwrap while the adjoin list is not empty
    
    while (total>0)
    {

        // Find the first non-empty skiplist in the adjoin-list
        
        for (bin=resumed, flag=1; flag==1 && bin>=0;)
        {
            if (adjoin_list[bin]!=NULL)
                flag = 0;
            else bin--;
        }
        
        
        // Step 5.1. Remove the highest pixel
        
        removeFirst(&index, &adjoin_list[bin], &list_last[bin]);
        total--;
        
        
        y = index/xsize;
        x = index%xsize;
        
        maxbin = 0;
        

        // Step 6. Examine its four neighbor pixels.
        
        // left neighbor
        a = x - 1;
        b = y;
        k = b*xsize + a;
        if (a>=0 && unwrap[k]==0 && mask[k]==1)
        {
            w = y*xsize + x-1;
            soln[k] = soln[index] + Gradient(phase[w], phase[w+1]);
            bin = mapping[k];
            insertSort(k, qual_map[k], &adjoin_list[bin], &list_last[bin], list_nodes);
            unwrap[k] = 1;
            //path[k] = iter++;
            total++;
            if (bin>maxbin) maxbin=bin;
        }


        // right neighbor
        a = x + 1;
        b = y;
        k = b*xsize + a;
        if (a < xsize && unwrap[k]==0 && mask[k]==1)
        {
            w = y*xsize + x;
            soln[k] = soln[index] - Gradient(phase[w], phase[w+1]);
            bin = mapping[k];
            insertSort(k, qual_map[k], &adjoin_list[bin], &list_last[bin], list_nodes);
            unwrap[k] = 1;
            //path[k] = iter++;
            total++;
            if (bin>maxbin) maxbin=bin;
        }
        
        // upper neighbor
        a = x;
        b = y - 1;
        k = b*xsize + a;
        if (b >= 0 && unwrap[k]==0 && mask[k]==1)
        {
            w = (y-1)*xsize + x;
            soln[k] = soln[index] + Gradient(phase[w], phase[w+xsize]);
            bin = mapping[k];
            insertSort(k, qual_map[k], &adjoin_list[bin], &list_last[bin], list_nodes);
            unwrap[k] = 1;
            //path[k] = iter++;
            total++;
            if (bin>maxbin) maxbin=bin;
        }
        
        
        // lower neighbor
        a = x;
        b = y + 1;
        k = b*xsize + a;
        if (b < ysize && unwrap[k]==0 && mask[k]==1)
        {
            w = y*xsize + x;
            soln[k] = soln[index] - Gradient(phase[w], phase[w+xsize]);
            bin = mapping[k];
            insertSort(k, qual_map[k], &adjoin_list[bin], &list_last[bin], list_nodes);
            unwrap[k] = 1;
            //path[k] = iter++;
            total++;
            if (bin>maxbin) maxbin=bin;
        }
        
        if (maxbin>resumed) resumed=maxbin;
    }
    
    
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &total_end);
    
    elapsed_time = (total_end.tv_sec - total_start.tv_sec)*1000.0 + (total_end.tv_nsec - total_start.tv_nsec)/ 1000000.0;
    
    
    
    
    /*  SAVE RESULT  */
    
    for (k=0; k<length; k++)
        soln[k] *= TWOPI;
    
    strcpy(prefix, data_path);
    strcat(prefix, "/I2L2/src/");
    strcat(prefix, pname);
    OpenFile(&ofp, prefix, "w");
    WriteFloat(ofp, soln, length, fname);
    
    // path inegration
    if (flag_debug)
    {
        strcpy(prefix, data_path);
        strcat(prefix, "/I2L2/src/");
        strcat(prefix, pname);
        strcat(prefix, ".path");
        SaveIntToImage(path, "path integration", prefix, xsize, ysize);
    }
    
    
    
    
    /* DEALLOCATE MEMORY */
    
    free(phase);
    free(qual_map);
    free(soln);
    free(unwrap);
    free(path);
    free(mask);
    
    free(adjoin_list);
    free(list_nodes);
    free(list_last);
    
    free(mapping);
    
    return elapsed_time;
}



int main()
{
    double elapsed_time=0;
    int    iter, max_iter=1;
    char data_path[1024];
    
    chdir("..");
    chdir("..");
    getcwd(data_path,1024);

    
    /*
     *   Peaks wrapped phase map, full precision.
     */
    int   num_levels    = 400;
    int   N             = 25;
    int   int_qual_flag = 0;
    float int_max_qual  = 1;
    int   flag_mask     = 0;
    int   flag_qual     = 1;

    
    for (iter=0; iter<max_iter; iter++)
    elapsed_time += Quality_guide_phase_unwrapping(data_path,"peaks512x512", 512, 512,
                                                   num_levels, N, flag_mask, flag_qual, int_qual_flag, int_max_qual);
    
    elapsed_time/=(double)max_iter;
    
    printf("\nAverage elapsed time: %f\n", elapsed_time);
    
    
    
    /*
     *  Plate PSI wrapped phase map, full precision.
     */
    /*
    int   num_levels    = 400;
    int   N             = 25;
    int   int_qual_flag = 0;
    float int_max_qual  = 255;
    int   flag_mask     = 1;
    int   flag_qual     = 1;

    
    for (iter=0; iter<max_iter; iter++)
        elapsed_time += Quality_guide_phase_unwrapping(data_path, "psi1404x1220", 1220, 1404,
                                                       num_levels, N, flag_mask, flag_qual, int_qual_flag, int_max_qual);
    
    elapsed_time/=(double)max_iter;
    
    printf("\nAverage elapsed time: %f\n", elapsed_time);
    */
    
    
    
    /*
     *  Rhino PSI wrapped phase map, full precision.
     */
    /*
     int   num_levels    = 400;
     int   N             = 25;
     int   int_qual_flag = 0;
     float int_max_qual  = 255;
     int   flag_mask     = 0;
     int   flag_qual     = 1;

    
     for (iter=0; iter<max_iter; iter++)
     elapsed_time += Quality_guide_phase_unwrapping(data_path, "rhino307x567", 307, 567,
     num_levels, N, flag_mask, flag_qual, int_qual_flag, int_max_qual);
     
     elapsed_time/=(double)max_iter;
     
     printf("\nAverage elapsed time: %f\n", elapsed_time);
    */
    
    return 0;
}
