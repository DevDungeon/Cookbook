#!/bin/bash

while read line ; do 
	pieces = (${line//\\// })
	filename = ${pieces[${#pieces[@]} - 1]}
	echo $filename
	#wget line pdf -o ./pdf/$(filename)
done

for line in pdflist.txt ; do
	echo $line
done
