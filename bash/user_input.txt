# Simple user prompt
echo -n "Enter name: "
read name
echo $name

# Read with a prompt
read -p "Enter name: " name
echo $name

# If reading from current shell and not running a separate process, use -e
read -e name

# Read with a default value
read -i "defaultName" name
