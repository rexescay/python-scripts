#!/usr/bin/python3

# image_sort.py - Walks directories from root folder and sorts files
# into apropriate directories
# python3 image_sort.py <path/to/root/directory>

import os, random, re, shutil, sys

if len(sys.argv) == 2:
	if os.path.isdir(sys.argv[1]):
		root_dir = sys.argv[1]
		if not root_dir.endswith('/'):
			root_dir += '/'
		os.chdir(root_dir)
else:
	print('# python3 image_sort.py <path/to/root/directory>')
	sys.exit()

suffix_re = re.compile(r'\.[a-z]{3,4}$')
suffix_list = []

# Walk filesystem from chosen root directory
for dir_names, sub_dirs, filenames in os.walk(root_dir):
	for files in filenames:
		# Check each file suffix using regex
		if suffix_re.search(files) != None:
			# each new suffix is saved in a list
			if suffix_re.search(files).group() not in suffix_list:
				suffix_list.append(suffix_re.search(files).group())

# new directory is created for each item in list
for s in suffix_list:
	s = s[1:]
	if os.path.exists(root_dir+s):
		print(s+' directory exists')
	else:
		print('Creating directory %s...'%s)
		os.makedirs(root_dir+s)

# each file is copied into appropriate directory
print(suffix_list)
for s in suffix_list:
	for dir_names, sub_dirs, filenames in os.walk(root_dir):
		for files in filenames:
			if files.endswith(s):
				print('Copying '+files+' to %s directory...' %s)
				new_dir = root_dir+s[1:]
				shutil.copy(files, new_dir)
