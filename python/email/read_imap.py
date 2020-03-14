# read_imap.py
# Connect to an SSL IMAP server and check mail
import getpass, imaplib

# Connect and login to IMAP mail server
username = 'me@example.com'
password = 'password'
mail_server = 'mail.example.com'
imap_server = imaplib.IMAP4_SSL(host=mail_server)
imap_server.login(username, password)

# List mailboxes (folders)
response_code, folders = imap_server.list()
print(response_code)  # OK
print('Available folders(mailboxes) to select:')
for folder_details_raw in folders:
    folder_details = folder_details_raw.decode().split()
    print(f'- {folder_details[-1]}')

# Create a mailbox
response_code, response_details = imap_server.create('INBOX.myfavorites')
print(response_code)  # OK on success or NO on failure
print(response_details)  # Create completed/Mailbox already exists
# Rename a mailbox
imap_server.rename('INBOX.myfavorites', 'INBOX.faves')
# Delete a mailbox
imap_server.delete('INBOX.faves')

# Choose the mailbox (folder) to search
# Case sensitive!
imap_server.select('INBOX')  # Default is `INBOX`

# Search for emails in the mailbox that was selected.
# First, you need to search and get the message IDs.
# Then you can fetch specific messages with the IDs.
# Search filters are explained in the RFC at:
# https://tools.ietf.org/html/rfc3501#section-6.4.4
search_criteria = 'ALL'
charset = None  # All
respose_code, message_numbers_raw = imap_server.search(charset, search_criteria)
print(f'Search response: {respose_code}')  # e.g. OK
print(f'Message numbers: {message_numbers_raw}')  # e.g. ['1 2'] A list, with string of message IDs
message_numbers = message_numbers_raw[0].split()

# Fetch full message based on the message numbers obtained from search
for message_number in message_numbers:
    response_code, message_data = imap_server.fetch(message_number, '(RFC822)')
    print(f'Fetch response for message {message_number}: {response_code}')
    #print(f'Raw email data:\n{message_data[0][1]}')

    # Mark an email read/unread.
    # Other flags you can set with store() from RFC3501 include: 
    # \Seen \Answered \Flagged \Deleted \Draft \Recent
    imap_server.store(message_number, '+FLAGS', '\SEEN')  # Mark as read
    imap_server.store(message_number, '-FLAGS', '\SEEN')  # Mark as unread

    # Copy an email to a different 
    imap_server.create('INBOX.mykeepers')
    imap_server.copy(message_number, 'INBOX.mykeepers')
    # Delete an email
    imap_server.store(message_number, '+FLAGS', '\Deleted')
    # Expunge after marking emails deleted
    imap_server.expunge()

imap_server.close()
imap_server.logout()
