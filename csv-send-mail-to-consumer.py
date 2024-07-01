from email.message import EmailMessage
import smtplib
import ssl
import csv
from time import sleep
import random

def send_mail_attachment(mail):

            toaddr = mail
            user = 'mail@example.com'
            passw = 'mail_password'
            smtp_server = 'smtp_server'
            port = 465
            subject = "Podziel się swoją opinią!"

            msg = EmailMessage()
            msg['From'] = user
            msg['To'] = toaddr
            msg['Subject'] = subject

            msg.set_type('text/html')
            msg.set_content("This is the Data Message that we want to send")
            html_msg = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Opinie</title>
</head>
<body>
    <h1>Mail in HTML</h1>
</body>
</html>
            """
            msg.add_alternative(html_msg, subtype="html")


            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(user, passw)
                server.send_message(msg)
            

            print("Mail sent to : " + toaddr)

filename = "consumers.csv"
with open(filename,'r+', encoding='utf-8-sig') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        mail = row['E-mail']
        send_mail_attachment(mail)
        rand_pause = random.randint(10, 40)
        sleep(rand_pause)
file.close()