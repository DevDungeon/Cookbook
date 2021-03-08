require 'gpgme'
# https://github.com/ueno/ruby-gpgme

path_to_key = "nanodano-public-key.txt" # If needed for import
path_to_encrypt = "message.txt"
output_path = "message.gpg"
recipient = "nanodano@devdungeon.com"

# This step is required if the local GPG does not have
# the public key for the recipient already
GPGME::Key.import(File.open(path_to_key)) 

crypto = GPGME::Crypto.new :always_trust => true

File.open(path_to_encrypt) do |in_file|
	File.open(output_path, 'wb') do |out_file|
		crypto.encrypt in_file, 
			:output => out_file,
			:recipients => recipient
			#symmetric => true
	end
end

#crypto.decrypt File.open("message.gpg")

#GPGME::Key.find(:secret, "someone@example.com")


#GPGME::Key.export("someone@example.com")
# => Returns a {GPGME::Data} object with the exported key.

#key = GPGME::Key.find(:secret, "someone@example.com").first
#key.export
# => Returns a {GPGME::Data} object with the exported key.