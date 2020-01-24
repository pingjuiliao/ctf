#!/usr/bin/python

from pwn import *

###           1      2
###   128                   4
###    64                   8
###           32    16




array = [i for i in range(0, 35)]
array[0] = 128 + 16 + 8
array[1] = 1 + 2 + 32 + 64
array[2] =


