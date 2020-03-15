from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64

from_email = 'John Leon <nanodano@devdungeon.com>'  # or simply the email address
to_emails = ['nanodano@devdungeon.com', 'johndleon@gmail.com']

# Create multipart MIME email
email_message = MIMEMultipart()
email_message.add_header('To', ', '.join(to_emails))
email_message.add_header('From', from_email)
email_message.add_header('Subject', 'Hello!')
email_message.add_header('X-Priority', '2')  # Urgent/High priority

# Create text and HTML bodies for email
text_part = MIMEText('Hello world plain text!', 'plain')
html_part = MIMEText('<html><body><h1>HTML!</h1></body></html>', 'html')

# Create file attachment
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(b'\xDE\xAD\xBE\xEF')  # Raw attachment data
encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment; filename=myfile.dat")

# Attach all the parts to the Multipart MIME email
email_message.attach(text_part)
email_message.attach(html_part)
email_message.attach(attachment)

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL('mail.example.com', port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login('user@email.com', 'password')
smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())

# Disconnect
smtp_server.quit()