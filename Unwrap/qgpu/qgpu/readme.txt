A pruning strategy to speedup the quality guide phase unwrapping algorithm by L. Lopez Garcia, W. Cruz Santos, A. Garcia Arellano and J. Rueda Paz sent to publish to Optics Express (2017).

This directory contains the source code and data files from the submitted paper.  See the LICENSE.txt file for the licensing statement and Disclaimer of Warranty.

The source code is written in C and C++ on the gcc and g++ compilers on a Desktop computer using Linux Ubuntu operating system. The organization of the directory qgpu is the following:

1. LL: Implementation of the quality guide phase unwrapping algorithm using an array for the adjoin list.

2. I2L2: Implementation of the quality guide phase unwrapping algorithm using a linked list for the adjoin list. 

3. Pruning: Implementation of the quality guide phase unwrapping algorithm with the pruning strategy.

4. data: Contains the wrapped phase maps, quality maps and mask files used in the submitted paper.

5. matlab. Contains matlab scripts to visualize the data files included in the data directory.


Compiling:

Each implementation of the QGPU algorithms in the directories LL, I2L2 and Pruning contain three directories, say include, lib and src. The header files in each implementation are in the include directory and the source files are in the src directory. To generate the executable program, locate in the corresponding src directory and type make in order to compile the project. To execute the program, type ./main in the current src directory.

The project can be compiled either in MAC OS x and in Linux operating systems.

 



