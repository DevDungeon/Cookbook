#!/bin/bash

# Simple user prompt
echo -n "Enter name: "
read name
echo "Hello, $name"

# Read with a prompt
read -p "Enter name: " name
echo "(read -p) Hello, $name"

# If reading from current shell and not running a separate process, use -e
echo -n "Enter name: "
read -e name
echo "(read -e) Hello, $name"

# Read with a default value
read -i "John Doe" -p "Enter name  (default: John Doe): " name
echo "(read -i) Name: $name"



# Infinite loop like when creating a menu or repeating
# until proper input is provided.
while true; do
  read -p "Exit? y/n " user_input
  if [[ $user_input == "y" ]]; then
    exit 0
  else
    echo "Please enter y"
  fi
done

