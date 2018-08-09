#!/usr/bin/sh

for files in * ; do
	# Makes directories based on the suffixes of files in root directory
	extentions=$(echo $files | cut -d '.' -f 2)
	if [ ! -d $extentions ] ; then
		mkdir $extentions
	fi
	mv $files $extentions
done
