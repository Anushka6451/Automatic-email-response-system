import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ACCOUNT, EMAIL_PASSWORD


# 🔹 Generate response from category
def generate_response(category):
    responses = {
        "refund": "Your refund request has been received and will be processed within 5-7 business days.",
        "delivery_issue": "We apologize for the delay. Your order is on the way.",
        "complaint": "We are sorry for the inconvenience caused.",
        "inquiry": "Thank you for contacting us. We will get back to you shortly.",
        "payment_issue": "We are checking your payment issue.",
        "return": "You can return the product within 7 days.",
        "cancellation": "Your cancellation request has been processed.",
        "update_request": "Your request will be updated shortly.",
        "technical_issue": "Our technical team is working on the issue.",
        "feedback": "Thank you for your valuable feedback!"
    }

    return responses.get(category, "Thank you for contacting us.")


# 🔹 UPDATED FUNCTION (IMPORTANT)
def send_response(to_email, subject, category):
    try:
        response_text = generate_response(category)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ACCOUNT
        msg["To"] = to_email
        msg["Subject"] = "Re: " + subject

        msg.attach(MIMEText(response_text, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

        server.send_message(msg)
        server.quit()

        print(f"✅ Sent to {to_email} | Category: {category}")

    except Exception as e:
        print(f"❌ Error: {e}")