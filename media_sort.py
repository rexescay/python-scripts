#!/usr/bin/python3

# image_sort.py - Walks directories from root folder and sorts files
# into apropriate directories
# python3 image_sort.py <path/to/root/directory>

import os, random, re, sys

if len(sys.argv) == 2:
	root_dir = sys.argv[1]
else:
	print('# python3 image_sort.py <path/to/root/directory>')
	sys.exit()

# Walk filesystem from chosen root directory
# Check each file suffix using regex
# each new suffix is saved in a list
# new directory is created for each item in list
# option to randomize filenames, not changing suffix
# each file is moved into appropriate directory
