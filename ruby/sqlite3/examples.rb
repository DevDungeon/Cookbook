# gem install sqlite3 # Install using Ruby
# sudo apt install ruby-sqlite3 # Debian
# sudo dnf install rubygem-sqlite3 # Fedora
require 'sqlite3'

db = SQLite3::Database.open 'test.db'
db.results_as_hash = true  # optional

## Executing
db.execute "CREATE TABLE IF NOT EXISTS images(path TEXT, thumbs_up INT)"
db.execute "INSERT INTO images (path, thumbs_up) VALUES (?, ?)", 'image1.png', 0

## Querying
results = db.query "SELECT path, thumbs_up FROM images WHERE path=?", image_path
# Alternatively, to only get one row and discard the rest,
# replace `db.query()` with `db.get_first_value()`.
first_result = results.next
if first_result
  puts first_result['thumb_up']
else
  puts 'No results found.'
end
# Alternatively, you can go through each result like this:
# results.each { |row| puts row.join(',') }

## Handling errors:
begin
    # Attempt some SQLite action
rescue SQLite3::Exception => e 
    # Handle the exception gracefully
ensure
    db.close if db # If catastrophic and exiting program, cleanup
end