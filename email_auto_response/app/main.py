import time
from app.email_reader import connect_imap, fetch_unseen_emails, parse_email
from app.email_sender import send_response
from app.database import save_email
from ML_model.predictions import predict_category

CHECK_INTERVAL = 30

def main():
    print("🔄 Connecting to email...")
    mail = connect_imap()
    print("✅ Connected successfully")

    print("📧 Auto email system started...")

    while True:
        print("🔍 Checking for new emails...")
        email_ids = fetch_unseen_emails(mail)

        print("📊 Fetch done")


        if email_ids:
            print(f"📥 Found {len(email_ids)} new email(s)")
        else:
            print("📭 No new emails")

        for e_id in email_ids:
            status, msg_data = mail.fetch(e_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):

                    from_, subject, body = parse_email(response_part[1])

                    if any(x in from_.lower() for x in [
                        "postmaster",
                        "mailer-daemon",
                        "no-reply",
                        "noreply"
                    ]):
                        continue

                    print(f"From: {from_}\nSubject: {subject}\nBody preview: {body[:50]}...\n")

                    category = predict_category(body)

                    save_email(from_, subject, category)

                    send_response(from_, subject, category)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()