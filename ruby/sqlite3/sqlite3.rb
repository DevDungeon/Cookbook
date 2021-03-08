#!/usr/bin/ruby

require 'sqlite3'

begin
    # Create db in memory. Replace :memory: with db file name    
    db = SQLite3::Database.new ":memory:"
    puts db.get_first_value 'SELECT SQLITE_VERSION()'
    
    #db.execute "CREATE TABLE IF NOT EXISTS tmp(id INTEGER PRIMARY KEY, \
    #  name TEXT)"

    # Insert example
    #db.execute "INSERT INTO tmp VALUES(1, 'stuff')
    
    # Get last inserted ID
    #last_id = db.last_insert_row_id

    # Retrieve data with prepared statement
    #stmt = db.prepare "SELECT * FROM tmp LIMIT 1" 
    #result = stmt.execute 
    #result.each do |row|
    #    puts row.join "\n"
    #end

rescue SQLite3::Exception => e 
    
    puts "Exception occured"
    puts e
    
ensure
    db.close if db
end
