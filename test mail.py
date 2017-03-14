import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'XXX@gmail.com'
msg['To'] = 'YYY@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('XXX@gmail.com', 'PASSWORD')
mailserver.sendmail('XXX@gmail.com', 'XXX@gmail.com', msg.as_string())
mailserver.quit()