import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(to, content):
    email_address = "topsis.mayank@gmail.com"
    email_password = "ifvbzrgdfqqcavaq"

    # create email
    msg = EmailMessage()
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Topsis Result File"
    msg['From'] = email_address
    msg['To'] = to 

    part = MIMEText(content, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        