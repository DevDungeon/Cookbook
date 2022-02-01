#!/bin/bash
# Present a list of accounts to choose from

exit_code=0

exec 3>&1

# Go back to the menu after quitting mutt
while [ $exit_code -eq 0 ]
do
  # Generate a menu of accounts
  choice=$(dialog --menu "Open mail" 40 40 40 \
           "~/.muttrc.1" "Account 1" \
           "~/.muttrc.2" "Account 2" \
           2>&1 1>&3)
  exit_code=$?
  if [ $exit_code -eq 0 ]
  then
    mutt -F "$choice"
  fi
done

exec 3>&-