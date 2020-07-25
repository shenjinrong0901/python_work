#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include "util.h"
#include "file.h"
#include "getqual.h"
#include "extract.h"
#include "maskfat.h"
#include "quality.h"
#include "pi.h"
#include "message.h"


#define BORDER (0x20)


float timedifference_msec(struct timeval t0, struct timeval t1)
{
    return (t1.tv_sec - t0.tv_sec) * 1000.0f + (t1.tv_usec - t0.tv_usec) / 1000.0f;
}


double QGPU(const char *data_path, const char *pname, const char *outf, const char *qfile,
            const char *mask_file, int xsize, int ysize, int flag_mask)
{
    int            i, j, k, p, kk;
    FILE           *ifp, *ofp, *mfp=0, *qfp=0;
    float          *phase;     /* array */
    float          *mask;
    float          *soln;      /* array */
    float          *qual_map;  /* array */
    unsigned char  *bitflags;  /* array */
    char           buffer[200], string[200];
    char           infile[200], outfile[200];
    char           bmaskfile[200], qualfile[200];
    char           tempstr[200], format[200], modekey[200];
    int            tsize, in_format, debug_flag, avoid_code;
    double         rmin, rmax, rscale;
    UnwrapMode     mode;
    int            list_size;
    float          *summary;
    int            num_steps, reps;
    int            *list_steps;
    
    struct timeval t0;
    struct timeval t1;
    float elapsed;
    
    
    
    printf("Phase Unwrapping by Quality Map Guided Path Following\n");
    
    
    
    /* GET COMMAND LINE PARAMETERS AND CHECK */
   
    in_format = 3;
    
    // phase input file
    strcpy(infile, data_path);
    strcat(infile,"/data/");
    strcat(infile, pname);
    
    // output file
    strcpy(outfile, data_path);
    strcat(outfile, "/LL/src/");
    strcat(outfile, outf);
    
    // quality input file
    strcpy(qualfile, data_path);
    strcat(qualfile,"/data/");
    strcat(qualfile,qfile);
    
    // mask input file
    strcpy(bmaskfile, data_path);
    strcat(bmaskfile,"/data/");
    strcat(bmaskfile,mask_file);
    
    printf("Format: %d\n", in_format);
    printf("Input file: %s\n", infile);
    printf("Output file: %s\n", outfile);
    printf("Quality file: %s\n",qualfile);
    printf("Mask file: %s\n",bmaskfile);

    
    /*
         OPEN FILES, ALLOCATE MEMORY
     */
    
    OpenFile(&ifp, infile, "r");
    OpenFile(&ofp, outfile, "w");
    OpenFile(&qfp, qualfile, "r");
    
    AllocateFloat(&phase, xsize*ysize, "phase data");
    AllocateFloat(&mask, xsize*ysize, "mask data");
    AllocateFloat(&soln, xsize*ysize, "unwrapped data");
    AllocateByte(&bitflags, xsize*ysize, "bitflag data");
    AllocateFloat(&qual_map, xsize*ysize, "quality map");
    
    
    /*
         READ AND PROCESS DATA
     */
    printf("Reading phase data...\n");
    GetPhase(in_format, ifp, infile, phase, xsize, ysize);
    
    if (qfp) {
        printf("Reading quality data...\n");
        GetPhase(3, qfp, "", qual_map, xsize, ysize);
    }
    
    
    list_size = xsize+ysize;
    printf("\nListSize: %d\nReps ...\n", list_size);
    
    
    
    if (flag_mask==1)
    {
        OpenFile(&mfp, bmaskfile, "r");
        GetPhase(3, mfp, "", mask, xsize, ysize);
        
        for (k=0; k<xsize*ysize; k++)
        {
            if (mask[k]>0)
                bitflags[k] = 255;
            else
                bitflags[k] = 0;
        }
    }
    else {
        for (k=0; k<xsize*ysize; k++)
        {
            bitflags[k] = 255;
	    mask[k] = 1;
        }
    }


    
    for (k=0; k<xsize*ysize; k++)
        bitflags[k] = (!bitflags[k]) ? BORDER : 0;
    FattenMask(bitflags, BORDER, 1, xsize, ysize);
    


    mode = gradient;
    printf("MODE %d\n", mode);
    
    
    /*
         initialize soln array
     */
    memset(soln, 0, sizeof(float)*xsize*ysize);
    
    
    
    /*  UNWRAP  */
    avoid_code = BORDER;
    if (mode==gradient && tsize==1)
        mode = dxdygrad;
    
    
    gettimeofday(&t0, 0);
    
    
    k = QualityGuidedPathFollower(phase, qual_map, bitflags, soln,
                                  xsize, ysize, avoid_code, mode, debug_flag, outfile, list_size);
    
    
    gettimeofday(&t1, 0);
    elapsed = timedifference_msec(t0, t1);
    
    printf("Code executed in %f milliseconds.\n", elapsed);
    
    
    if (k > 1) printf("\n%d pieces\n", k);
    
    printf("\nFinished\n");
    PrintMinAndMax(xsize, ysize, soln, "solution");
    
    /*  SAVE RESULT  */
    /* scale output */
    for (k=0; k<xsize*ysize; k++)
        soln[k] *= TWOPI;
    
    printf("Saving unwrapped surface to file '%s'\n", outfile);
    WriteFloat(ofp, soln, xsize*ysize, outfile);
    
    
    free(soln);
    free(phase);
    free(bitflags);
    free(qual_map);
    
    return elapsed;
}



int main()
{
    char data_path[1024];
    
    chdir("..");
    chdir("..");
    getcwd(data_path,1024);
    
    // Experimente 1: peaks wrapped phase map
    
    int k, NUM_ITER = 20;
    double elapsed=0;
    
    for (k=0; k<NUM_ITER; k++)
        elapsed+=QGPU(data_path, "peaks512x512.phase", "peaks512x512", "peaks512x512.qual",
                "", 512, 512, 0);
    elapsed = elapsed / (double)NUM_ITER;
    
    printf("\nAverage time: %f\n", elapsed);
    
    
    
    // Experimente 2: plate wrapped phase map
    /*
     int k, NUM_ITER = 20;
     double elapsed=0;
     
     for (k=0; k<NUM_ITER; k++)
         elapsed+=QGPU(data_path, "psi1404x1220.phase", "psi1404x1220", "psi1404x1220.qual",
     "psi1404x1220.mask", 1220, 1404, 1);
     elapsed = elapsed / (double)NUM_ITER;
     
     printf("\nAverage time: %f\n", elapsed);
    */
    
    // Experimente 3: rhino wrapped phase map
    /*
     int k, NUM_ITER = 20;
     double elapsed=0;
     
     for (k=0; k<NUM_ITER; k++)
     elapsed+=QGPU(data_path, "rhino307x567.phase", "rhino307x567", "rhino307x567.qual",
     "rhino307x567.mask", 307, 567, 1);
     elapsed = elapsed / (double)NUM_ITER;
     
     printf("\nAverage time: %f\n", elapsed);
    */
    
    
    return 0;
}
