#!/usr/bin/python3

# python3 regex_search.py <expression> <directory path>
# Searches '.txt' files in <directory path> and returns all lines
# containing <expression>

import os, re, sys

# Inturpret command line arguments.
if len(sys.argv) == 3:
	if os.path.exists(str(sys.argv[2])):
		directory_path = str(sys.argv[2])
	else:
		directory_path = '.'
	regex = re.compile(sys.argv[1], re.IGNORECASE)
elif len(sys.argv) == 2:
	directory_path = '.'
	regex = re.compile(sys.argv[1])
else:
	print("# python3 regex_search.py <expression> <directory path>\n# Searches '.txt' files in <directory path> and returns all lines\n# containing <expression>")
	sys.exit()

# Find appropriate files in the path provided.
for txt_file in os.listdir(directory_path):
	if os.path.isfile(txt_file):
		# Read contents of the file
		file_object = open(txt_file)
		file_content = file_object.read()
		# Print lines that matched regular expression
		if regex.search(file_content) != None:
			print('-'*5+txt_file+'-'*5)
			lines = file_content.split('\n')
			for matched_lines in lines:
				if regex.search(matched_lines) != None:
					print(matched_lines.strip())
