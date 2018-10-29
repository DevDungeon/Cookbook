require 'active_record'
require 'mysql2' #'mysql2' or 'pg' or 'sqlite3'

# Database settings
ActiveRecord::Base.establish_connection(
  # How to do a sqlite in memory?
  adapter:  'mysql2', # or 'postgresql' or 'sqlite3'
  host:     'localhost',
  database: 'test',
  username: 'test',
  password: 'test'
)


# Define your classes based on the database
# Table is users, needs primary key id auto_increment
class User < ActiveRecord::Base
  # Set relationships here if needed
  #has_many                :posts
end


# Create new user
new_user = User.new
new_user.name = "Test user"
new_user.save
puts new_user

# Create new user another way
new_user2 = User.create(name: "Test user2")
puts new_user2

# Queries
puts User.find(1).inspect
puts User.first.inspect
puts User.last.inspect
puts User.all.inspect
puts User.find_by(name: "Test user2").inspect # Finds first

