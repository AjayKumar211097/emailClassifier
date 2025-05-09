# backend/emailservice/mailer.py

def send_email(recipient: str, subject: str, body: str):
    """
    Dummy mailer. Replace with real SMTP or email-sending library.
    """
    print(f"--- Sending Email ---")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")
    print(f"---------------------")
