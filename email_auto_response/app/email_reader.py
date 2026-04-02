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
    return messages[0].split()


def decode_text(text):
    decoded_parts = decode_header(text)
    result = ""

    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            try:
                result += part.decode(encoding or "utf-8")
            except:
                result += part.decode("latin-1", errors="ignore")
        else:
            result += part

    return result


def parse_email(raw_email):
    msg = email.message_from_bytes(raw_email)

    from_ = msg["From"]
    subject = decode_text(msg["Subject"] or "")

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()

            if content_type == "text/plain":
                payload = part.get_payload(decode=True)

                if payload:
                    try:
                        body = payload.decode("utf-8")
                    except:
                        body = payload.decode("latin-1", errors="ignore")
                break
    else:
        payload = msg.get_payload(decode=True)

        if payload:
            try:
                body = payload.decode("utf-8")
            except:
                body = payload.decode("latin-1", errors="ignore")

    # Clean HTML
    body = BeautifulSoup(body, "html.parser").get_text()

    return from_, subject, body