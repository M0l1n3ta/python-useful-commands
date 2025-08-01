# Python script to send personalized emails to a list of recipients
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = 'r069965@gmail.com'

def send_personalized_email(sender_email, sender_password, recipients, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    for recipient_email in recipients:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()

_body = "<h1>Prueba Python<\h1>"
send_personalized_email(sender_email,"lfot gupn zrtc axke",['EmilioJRoldan@gmail.com'],"Prueba Python",_body)