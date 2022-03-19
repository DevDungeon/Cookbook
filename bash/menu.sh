#!/bin/bash

present_menu() {
    echo "============ Menu ========="
    echo "  1) Greet me"
    echo "  q) Quit"
    echo "==========================="
    echo ""
    echo -n "Enter your choice: "
}

handle_choice() {
  if [[ "$1" == "q" ]]; then
    echo "See you later!"
    exit 0
  elif [[ "$1" == "1" ]]; then
    echo "**********************************"
    echo "**          Hello!!             **"
    echo "**********************************"
  else
    echo "**********************************"
    echo "** Please enter a valid choice. **"
    echo "**********************************"
  fi
}

main() {
  clear
  while true; do
    present_menu
    read choice
    clear
    handle_choice "$choice"
  done
}

main


