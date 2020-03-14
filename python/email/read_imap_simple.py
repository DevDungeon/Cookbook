import imaplib
import email

imap_server = imaplib.IMAP4_SSL(host='mail.example.com')
imap_server.login('user', 'pass')

imap_server.select()  # Default is `INBOX`

# Find all emails in inbox and print out the raw email data
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, '(RFC822)')
    # Parse the raw email message in to a convenient object
    message = email.message_from_bytes(msg[0][1])
    
    print('== Email message =====')
    print(message)
    print('== Email details =====')
    print(f'Object type: {type(message)}')
    print(f'Content type: {message.get_content_type()}')
    # Content disposition will tell type, if is attachment, filename, size
    print(f'Content disposition: {message.get_content_disposition()}')
    print(f'Multipart?: {message.is_multipart()}')
    # If the message is multipart, it basically has multiple emails inside
    # so you must extract each "submail" separately.
    if message.is_multipart():
        print('Multipart types:')
        for part in message.walk():
            print(f'- {part.get_content_type()}')
        multipart_payload = message.get_payload()
        for sub_message in multipart_payload:
            # The actual text/HTML email contents, or attachment bytes
            print(f'Multipart Payload\n{sub_message.get_payload()}')
    else:  # Not a multipart message, payload is simple string
        print(f'Payload\n{message.get_payload()}')
