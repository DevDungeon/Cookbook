#!/usr/bin/ruby

# Must gem install mysql first

require 'mysql'

begin
    con = Mysql.new 'localhost', 'root', ''
#    puts con.get_server_info # Prints version same as next lines
    rs = con.query 'SELECT VERSION()'
    puts rs.fetch_row 
    
rescue Mysql::Error => e
    puts e.errno
    puts e.error
    
ensure
    con.close if con
end
