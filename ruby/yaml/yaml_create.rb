require 'yaml'

# Collection
puts( [ 'dogs', 'cats', 'badgers' ].to_yaml )

# Mapping
puts( { 'dog' => 'canine',
        'cat' => 'feline',
        'badger' => 'malign' }.to_yaml )