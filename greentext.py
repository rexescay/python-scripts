#!/usr/bin/python3

# Add '>' to the beginning of each line of text on the clipboard
# For convenience when using 4chan

import pyperclip

# Get the text from the clipboard
text = pyperclip.paste()

# Turn it into green text
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '>' + lines[i]

# Print to clipboard and give appropriate message when completed
text = '\n'.join(lines)
pyperclip.copy(text)
print('Text on clipboard has been converted to green text')
