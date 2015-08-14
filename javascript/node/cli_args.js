// Access specific arguments
console.log(process.argv[0]);
console.log(process.argv[1]);
console.log(process.argv[2]);

// Iterate through all arguments
process.argv.forEach(function(val, index, array) {
  console.log(index + ': ' + val);
});
