console.log(process.argv[0]);
console.log(process.argv[1]);
console.log(process.argv[2]);

process.argv.forEach(function(val, index) {
    console.log(index + ": " + val);
});
