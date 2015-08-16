# CoffeeScript Examples
# See coffeescript.org for more info

# To compile, install coffee-script package for Node.js
# npm install coffee-script

# Compile with
# coffee -c src.coffee

# Run with
# coffee src.coffee


# Creating an Object
rectangle =
  area:   (length, width) -> length * width
  perimeter: (length, width) -> length * 2 + width * 2

console.log rectangle.area(5, 4)
console.log rectangle.perimeter(100, 4)
