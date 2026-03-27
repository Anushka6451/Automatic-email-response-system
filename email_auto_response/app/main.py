# main.py

import time
from app.email_reader import connect_imap, fetch_unseen_emails, parse_email
from app.email_sender import send_response

CHECK_INTERVAL = 30  # seconds

def main():
    mail = connect_imap()
    print("📧 Auto email system started...")
    
    while True:
        email_ids = fetch_unseen_emails(mail)
        if email_ids:
            print(f"📥 Found {len(email_ids)} new email(s)")
        for e_id in email_ids:
            status, msg_data = mail.fetch(e_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    from_, subject, body = parse_email(response_part[1])
                    print(f"From: {from_}\nSubject: {subject}\nBody preview: {body[:50]}...\n")
                    send_response(from_, subject)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()