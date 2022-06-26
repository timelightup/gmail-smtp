import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

# email content placeholder

content = '--------------<br>'
content += ('Hello Gmail')
content += ('<br>--------------<br>')
content +=('<br><br>End of Message')

print('Composing Email...')

# update your email details
SERVER = 'smtp.gmail.com' # "your smtp server"
PORT = 587 # your port number
FROM =  '' # "your from email id"
TO = '' # "your to email ids"  # can be a list
PASS = '' # "your email id's password"

msg = MIMEMultipart()

msg['Subject'] = '[Automated Email] Python SMTP' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()