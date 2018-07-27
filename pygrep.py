#!/usr/bin/python3

# python3 regex_search.py <expression> <directory path>
# Searches '.txt' files in <directory path> and returns all lines
# containing <expression>

import os, re, sys, pprint

# Inturpret command line arguments.
if len(sys.argv) == 3:
	if os.path.exists(str(sys.argv[2])):
		directory_path = str(sys.argv[2])
	else:
		directory_path = '.'
	regex = re.compile(sys.argv[1])
elif len(sys.argv) == 2:
	directory_path = '.'
	regex = re.compile(sys.argv[1])
else:
	print("# python3 regex_search.py <expression> <directory path>\n# Searches '.txt' files in <directory path> and returns all lines\n# containing <expression>")
	sys.exit()

# Find appropriate files in the path provided.
file_type = re.compile(r'\.txt$')
line_list = []
for txt_file in os.listdir(directory_path):
	if os.path.isfile(txt_file) and file_type.search(txt_file) != None:
		# Read each file and store matching lines in a list
		file_object = open(txt_file)
		for matched_lines in file_object.readlines():
			if regex.search(matched_lines) != None:
				line_list.append(matched_lines)

for lines in line_list:
	print(lines, end='')
