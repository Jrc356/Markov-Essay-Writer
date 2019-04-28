#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: ./rename <folder/to/rename/files>"
	exit 1
fi

dir=$1

cd "${dir}"

ext=0
for file in ./*; do
	echo $file
	mv "${file}" "essay_${ext}.txt"
	ext=$((ext + 1))
done
