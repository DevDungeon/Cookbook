from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.message import EmailMessage

# Craft the email using email.message.EmailMessage
from_email = 'John Leon <nanodano@devdungeon.com>'  # or simply the email address
to_emails = ['nanodano@devdungeon.com', 'admin@devdungeon.com']
email_message = EmailMessage()
email_message.add_header('To', ', '.join(to_emails))
email_message.add_header('From', from_email)
email_message.add_header('Subject', 'Hello!')
email_message.add_header('X-Priority', '2')  # Urgent/High priority
email_message.set_content('Hello, world!')

# Connect, authenticate, and send mail
smtp_server = SMTP_SSL('mail.example.com', port=SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)  # Show SMTP server interactions
smtp_server.login('user@example.com', 'pass')
smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())

# Disconnect
smtp_server.quit()