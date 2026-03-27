# email_reader.py

import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup

from config import EMAIL_ACCOUNT, EMAIL_PASSWORD, IMAP_HOST

def connect_imap():
    mail = imaplib.IMAP4_SSL(IMAP_HOST)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select("inbox")
    return mail

def fetch_unseen_emails(mail):
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    return email_ids

def parse_email(msg_bytes):
    msg = email.message_from_bytes(msg_bytes)
    
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    
    from_ = msg.get("From")
    
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
            elif part.get_content_type() == "text/html" and not body:
                html = part.get_payload(decode=True).decode()
                body = BeautifulSoup(html, "html.parser").get_text()
    else:
        body = msg.get_payload(decode=True).decode()
    
    return from_, subject, body