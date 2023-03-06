import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

fromadd = 'vaxer.solutions@gmail.com'
password = 'rnjnuaxczxnagewj'
toadd = 'nksiddhi20@gmail.com'
sub = "Today's data"
content = "Today's birth info"
msg = MIMEMultipart()
msg['from'] = fromadd
msg['to'] = toadd
msg['subject'] = sub
body = MIMEText(content, 'plain')
msg.attach(body)
file = 'vaxer_dummy_db.csv'
f = open(file, 'r')
a = MIMEApplication(f.read(), Name=basename(file))
a['Content-Disposition'] = 'a; file = "{}"'.format(basename(file))
msg.attach(a)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(fromadd, password)
server.send_message(msg)
server.quit()
