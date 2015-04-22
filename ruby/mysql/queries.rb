#!/usr/bin/ruby

# Must gem install mysql first

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', ''

    # puts con.get_server_info # Prints version same as next lines

    rs = con.query 'SELECT VERSION()'
    puts rs.fetch_row    

    #con.query("CREATE TABLE tmp(id INT PRIMARY KEY AUTO_INCREMENT, \
    #    name VARCHAR(255))")

    #con.query("INSERT INTO tmp(name) VALUES('xyz')")

    #result = con.query("SELECT * FROM tmp")
    #num_rows = result.num_rows
    #puts "Result has #{num_rows} rows"
    #num_rows.times do
    #    puts result.fetch_row.join("\n")
    #end
    
rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
