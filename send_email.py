import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, recipient, subject, body, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return False
