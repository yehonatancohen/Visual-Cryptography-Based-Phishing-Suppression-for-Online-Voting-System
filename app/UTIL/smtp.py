import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

def send_image_email(recipient_email, subject, message, image_path):
    load_dotenv('smtp.env')
    # Create an SMTP instance
    smtp_server = os.getenv('MAIL_HOST', 'smtp.gmail.com')
    smtp_port = os.getenv('MAIL_PORT', 587)
    smtp_username = os.getenv('MAIL_USERNAME')
    sender_password = os.getenv('MAIL_PASSWORD')

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, sender_password)

        # Create a MIME object to represent the email
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add text message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Add image attachment to the email
        with open(image_path, 'rb') as file:
            img_data = file.read()
            image = MIMEImage(img_data, name='image.jpg')
            msg.attach(image)

        # Send the email
        server.sendmail(smtp_username, recipient_email, msg.as_string())

        # Close the SMTP server connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

# Usage example
if __name__ == "__main__":
    recipient_email = "yoncohenyon@gmail.com"
    subject = "Image Email"
    message = "Here's an image attached."
    image_path = "image.jpg" 

    send_image_email(recipient_email, subject, message, image_path)
