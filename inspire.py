#!/usr/bin/python3

# inspire.py - Tracks my no-fap progress and allows the inclusion of achievements

import os, shelve, sys

# Creates a shelve file which stores variables
path = '/home/rex/.scripts/'
if not os.path.exists(path+'inspire.data'):
	sf = shelve.open(path+'inspire.data')
	sf['days'] = 0
	d = {}
	sf['dictionary'] = d
	sf.close()

if len(sys.argv) == 2:
	if int(sys.argv[1]) == 1:
		print('Another Win!')
		sf = shelve.open(path+'inspire.data')
		sf['days'] += 1
elif len(sys.argv) == 1:
	print('Stay strong bro.')
	sf = shelve.open(path+'inspire.data')
else:
	print('Strange arguments...')
	sys.exit()

sf.close()
