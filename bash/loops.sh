#!/bin/bash

#####################
## For loops ###
###################

# Specific number of iterations
for i in $(seq 1 10)
do
  echo "$i"
done

# Specify list of files
for x in test.txt misc.txt other.txt
do
	echo "$x"
done

# For each file
FILES="file1.txt
file2.txt
file3.txt"
for f in $FILES; do echo "$f"; done

# For each file
for f in *.txt; do echo "$f"; done

# Traditional for loop
for (( c=1; c<=5; c++ ))
do
	echo "hi"
done


#########################
## While loops ####
#################



# Go through each CLI arg until there are no more
while [ $# -gt 0 ]; do
  echo $1
  shift
done


while true; do
  read -p "Exit? y/n " user_input
  if [[ $user_input == "y" ]]; then exit 0; fi
done
