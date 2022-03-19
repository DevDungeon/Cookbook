#!/bin/bash

# $@ - Array of args Arg 0 is script itself e.g.  ./cli_args.sh or cli_args.sh
# $# - Number of args passed  0 if no args passed to script (excludes arg 0)
# $0, $1, $2 - Directly address args passed.


echo "You provided the arguments:" "$@"

# You could pass all arguments to another program like this
# myProgram "$@"

echo "You provided $# arguments"

echo "Arg 0: $0"
echo "Arg 1: $1"
echo "Arg 2: $2"

for arg in "$@"
do
    echo "$arg"
done

for arg in "$@"
do
    if [ "$arg" == "--help" ] || [ "$arg" == "-h" ]
    then
        echo "Help argument detected."
    fi
done


# Go through all args provided
while [ $# -gt 0 ]; do
  echo $1
  shift
done

