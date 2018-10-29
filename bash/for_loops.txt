# Specific number of iterations
for i in $(seq 1 10)
do
  echo $i
done

# Specify list
for x in test.txt misc.txt other.txt
do
	rm $x
done

# Traditional for loop
for (( c=1; c<=5; c++ ))
do
	echo "hi"
done