#!/usr/bin/python3

import os, pyperclip, pprint

# Get copied text from clipboard
location = os.path.abspath('.')
copied_text = pyperclip.paste()

# Create a file with copied text
file_object = open('file.txt', 'w')
file_object.write(copied_text)
file_object.close()

print('Successfully coppied text to \'file.txt\' at ' + location + '.')
