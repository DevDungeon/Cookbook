require 'openssl'

# Generate new pub/private key pair
key = OpenSSL::PKey::RSA.new 2048
open 'private_key.pem', 'w' do |io| 
	io.write key.to_pem 
end
open 'public_key.pem', 'w' do |io|
	io.write key.public_key.to_pem
end

# To password protect the key
#OpenSSL::Cipher.ciphers # Lists available ciphers
cipher = OpenSSL::Cipher.new 'AES-128-CBC'
pass_phrase = 'passphrase here'
key_secure = key.export cipher, pass_phrase

open 'private.secure.pem', 'w' do |io|
  io.write key_secure
end

# Open an existing key and see if it is public or private
key2 = OpenSSL::PKey::RSA.new File.read 'private_key.pem'
puts key2.public? # => true
puts key2.private? # => true # private keys can be both pub and private

key3 = OpenSSL::PKey::RSA.new File.read 'public_key.pem'
puts key3.private? # => false # pub keys are public only

# Open a secure key
key4_pem = File.read 'private.secure.pem'
key4 = OpenSSL::PKey::RSA.new key4_pem, pass_phrase # without pass_phrase, will be prompted for pass