
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_share(email, share):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("cyberbtask2@gmail.com", "leontheking123s")
    # need to continue sending emails.
    pass