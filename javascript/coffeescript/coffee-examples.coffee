# CoffeeScript Examples
# See coffeescript.org for more info

# To compile, install coffee-script package for Node.js
# npm install coffee-script

# Compile with
# coffee -c src.coffee

# Run with
# coffee src.coffee

# Assignment:
number   = 42
opposite = true
console.log number

# Conditions:
number = -42 if opposite
console.log number

# Functions:
square = (x) -> x * x
console.log square(4)


# Arrays:
list = [1, 2, 3, 4, 5]

# Objects:
math =
  root:   Math.sqrt
  square: square
  cube:   (x) -> x * square x

# Splats:
race = (winner, runners...) ->
  print winner, runners

# Existence:
console.log "I knew it!" if elvis?

# Array comprehensions:
cubes = (math.cube num for num in list)

console.log "Done."
