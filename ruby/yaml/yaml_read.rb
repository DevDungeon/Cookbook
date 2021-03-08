require 'yaml'

# Loads yaml file in to a hash
config = YAML.load_file("config.yaml")

puts config["dog"]
puts config["cat"]
puts config["badger"]