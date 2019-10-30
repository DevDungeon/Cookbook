import smtplib

server = smtplib.SMTP('mail.devdungeon.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login('nanodano@devdungeon.com', 'mypass!')

server.sendmail('from@devdungeon.com',
                ['nanodano@devdungeon.com', 'webmaster@devdungeon.com'],
                'Email content')
