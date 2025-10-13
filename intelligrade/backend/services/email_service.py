import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_reset_email(to_email: str, reset_token: str):
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    from_email = smtp_user
    
    reset_link = f"https://your-frontend-url.com/reset-password?token={reset_token}"
    subject = "Password Reset Request"
    body = f"""
    <p>Hello,</p>
    <p>You requested a password reset. Click the link below to reset your password:</p>
    <a href='{reset_link}'>{reset_link}</a>
    <p>If you did not request this, please ignore this email.</p>
    """
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
