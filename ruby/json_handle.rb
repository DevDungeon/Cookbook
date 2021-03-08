require 'json'

# Parse JSON to hash
json = JSON.parse('{"color": "red"}')
puts json["color"]

# Generate JSON from hash
hash = {:color => "blue"}
puts JSON.generate(hash)
