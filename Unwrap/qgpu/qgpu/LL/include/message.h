/* User program message */

char use_program[] =      /* define usage statement */
"Usage: prog-name -input file -format fkey -output file\n"
"  -xsize x -ysize y -mode mkey [ -bmask file -corr file\n"
"  -tsize size -debug yes/no]\n"
"where 'fkey' is a keyword designating the input file type\n"
"(key = complex8, complex4, float or byte), 'x' and 'y' are\n"
"the dimensions of the file, bmask is an optional byte-file\n"
"of masks for masking out undefined phase values, corr\n"
"is an optional byte-file of cross-correlation values,\n"
"tsize is the size of the square template for averaging the\n"
"corr file or quality values (default = 1), and 'mkey' is\n"
"a keyword designating the source of the quality values\n"
"that guide the unwrapping path.  The value of mkey must be\n"
"'min_grad' for Minimum Gradient unwrapping, 'min_var' for\n"
"Minimum Variance unwrapping, 'max_corr' for Maximum\n"
"Correlation unwrapping, or 'max_pseu' for Maximum\n"
"Pseudocorrelation unwrapping.  All files are simple\n"
"raster files, and the output file consists of floating\n"
"point numbers that define the heights of the unwrapped\n"
"surface.  If the 'debug' parm is 'yes', then intermediate\n"
"byte-files are saved (quality map, unwrapping paths, etc.)\n";