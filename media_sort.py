#!/usr/bin/python3

# image_sort.py - Walks directories from root folder and sorts files
# into apropriate directories
# python3 image_sort.py <path/to/root/directory>

import os, random, re, shutil, sys

if len(sys.argv) == 2:
	if os.path.isdir(sys.argv[1]):
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

suffix_re = re.compile(r'\.[a-z]{3,4}$')
suffix_list = []

for dir_names, sub_dirs, filenames in os.walk(root_dir):
	for files in filenames:
		if suffix_re.search(files) != None:
			if suffix_re.search(files).group() not in suffix_list:
				suffix_list.append(suffix_re.search(files).group())

for s in suffix_list:
	if os.path.exists(root_dir+s[1:]):
		print(s[1:]+' directory exists')
	else:
		print('Creating directory %s...'%s[1:])
		os.makedirs(root_dir+s[1:])
