# email_sender.py

import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ACCOUNT, EMAIL_PASSWORD, SMTP_HOST, SMTP_PORT

def send_response(to_email, original_subject, response_text=None):
    reply_subject = f"Re: {original_subject}"
    body = response_text if response_text else "Hello, we received your email and will respond shortly. Thank you!"
    
    msg = MIMEText(body)
    msg["From"] = EMAIL_ACCOUNT
    msg["To"] = to_email
    msg["Subject"] = reply_subject

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ACCOUNT, to_email, msg.as_string())
    
    print(f"✅ Response sent to: {to_email} | Subject: {reply_subject}")