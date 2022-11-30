import os
import smtplib
from email.message import EmailMessage

email_address = os.environ.get("alt_email_username")
email_password = os.environ.get("alt_email_password_app")


msg = EmailMessage()
msg["Subject"] = "test message 2"
msg["From"] = email_address
msg["To"] = "splashtiger117@gmail.com"
msg.set_content("This is another test message from me")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(email_address, email_password)

    smtp.send_message(msg)

