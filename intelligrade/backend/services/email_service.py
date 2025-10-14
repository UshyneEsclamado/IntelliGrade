import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the backend directory
backend_dir = Path(__file__).parent.parent
env_path = backend_dir / '.env'
load_dotenv(dotenv_path=env_path)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_email_config():
    """Get email configuration from environment variables"""
    return {
        'smtp_server': os.getenv("SMTP_SERVER", "smtp.gmail.com"),
        'smtp_port': int(os.getenv("SMTP_PORT", 587)),
        'smtp_user': os.getenv("SMTP_USER"),
        'smtp_password': os.getenv("SMTP_PASSWORD"),
        'from_name': os.getenv("FROM_NAME", "IntelliGrade Support"),
        'from_email': os.getenv("FROM_EMAIL", "noreply@intelligrade.com"),
        'frontend_url': os.getenv("FRONTEND_URL", "http://localhost:5174"),
        'send_real_emails': os.getenv("SEND_REAL_EMAILS", "true").lower() == "true",
        'email_debug': os.getenv("EMAIL_DEBUG", "false").lower() == "true"
    }

def is_email_configured() -> bool:
    """Check if email is properly configured for sending"""
    config = get_email_config()
    return bool(config['smtp_user'] and config['smtp_password'])

def create_reset_email_html(reset_link: str, user_email: str) -> str:
    """Create a professional HTML email template for password reset"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Reset - IntelliGrade</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f5f5f5; }}
            .container {{ max-width: 600px; margin: 0 auto; background-color: white; }}
            .header {{ background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%); padding: 30px; text-align: center; }}
            .logo {{ color: white; font-size: 28px; font-weight: bold; margin: 0; }}
            .content {{ padding: 40px 30px; }}
            .title {{ color: #3D8D7A; font-size: 24px; font-weight: 600; margin-bottom: 20px; }}
            .message {{ color: #666; line-height: 1.6; margin-bottom: 30px; }}
            .button {{ display: inline-block; background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%); color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: 600; margin: 20px 0; }}
            .button:hover {{ opacity: 0.9; }}
            .footer {{ background-color: #f8f9fa; padding: 20px 30px; text-align: center; color: #666; font-size: 14px; }}
            .warning {{ background-color: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 5px; margin: 20px 0; color: #856404; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 class="logo">🎓 IntelliGrade</h1>
            </div>
            <div class="content">
                <h2 class="title">Password Reset Request</h2>
                <p class="message">Hello,</p>
                <p class="message">
                    We received a request to reset the password for your IntelliGrade account (<strong>{user_email}</strong>).
                </p>
                <p class="message">
                    Click the button below to reset your password. This link will expire in 1 hour for security reasons.
                </p>
                <div style="text-align: center;">
                    <a href="{reset_link}" class="button">Reset My Password</a>
                </div>
                <p class="message">
                    If the button doesn't work, you can copy and paste this link into your browser:
                    <br><a href="{reset_link}" style="color: #3D8D7A;">{reset_link}</a>
                </p>
                <div class="warning">
                    <strong>⚠️ Security Notice:</strong> If you didn't request this password reset, please ignore this email. Your password will remain unchanged.
                </div>
            </div>
            <div class="footer">
                <p>© 2025 IntelliGrade. All rights reserved.</p>
                <p>This is an automated email. Please do not reply to this email.</p>
            </div>
        </div>
    </body>
    </html>
    """

def send_reset_email(to_email: str, reset_token: str) -> bool:
    """Send password reset email with improved error handling and logging"""
    try:
        config = get_email_config()
        
        # Check if SMTP is configured
        if not config['smtp_user'] or not config['smtp_password']:
            logger.warning("SMTP credentials not configured. Cannot send email.")
            return False
        
        # Create the reset link
        reset_link = f"{config['frontend_url']}/reset-password?token={reset_token}"
        
        # Create email message
        msg = MIMEMultipart('alternative')
        msg["From"] = f"{config['from_name']} <{config['smtp_user']}>"
        msg["To"] = to_email
        msg["Subject"] = "🔐 Password Reset Request - IntelliGrade"
        
        # Create HTML content
        html_content = create_reset_email_html(reset_link, to_email)
        
        # Create text version as fallback
        text_content = f"""
IntelliGrade - Password Reset Request

Hello,

We received a request to reset the password for your IntelliGrade account ({to_email}).

Click this link to reset your password (expires in 1 hour):
{reset_link}

If you didn't request this password reset, please ignore this email.

© 2025 IntelliGrade. All rights reserved.
        """
        
        # Attach both versions
        msg.attach(MIMEText(text_content, 'plain'))
        msg.attach(MIMEText(html_content, 'html'))
        
        # Send email
        logger.info(f"Attempting to send password reset email to {to_email}")
        
        with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
            server.starttls()
            server.login(config['smtp_user'], config['smtp_password'])
            server.sendmail(config['smtp_user'], to_email, msg.as_string())
        
        logger.info(f"✅ Password reset email sent successfully to {to_email}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"❌ SMTP Authentication failed: {e}")
        return False
    except smtplib.SMTPRecipientsRefused as e:
        logger.error(f"❌ Invalid recipient email {to_email}: {e}")
        return False
    except smtplib.SMTPServerDisconnected as e:
        logger.error(f"❌ SMTP server disconnected: {e}")
        return False
    except Exception as e:
        logger.error(f"❌ Failed to send email to {to_email}: {e}")
        return False

def send_password_reset_email_production(to_email: str, reset_token: str) -> dict:
    """Production-ready email sending with real email priority"""
    config = get_email_config()
    reset_link = f"{config['frontend_url']}/reset-password?token={reset_token}"
    
    # Always try real email first if configured
    if config['send_real_emails'] and is_email_configured():
        try:
            success = send_reset_email(to_email, reset_token)
            if success:
                logger.info(f"📧 Real email sent successfully to {to_email}")
                return {
                    "success": True,
                    "method": "email",
                    "message": "A password reset link has been sent to your email address."
                }
            else:
                logger.warning(f"⚠️ Real email failed for {to_email}")
                return {
                    "success": False,
                    "method": "failed",
                    "message": "Failed to send reset link. Please try again later."
                }
        except Exception as e:
            logger.error(f"❌ Email sending error: {e}")
            return {
                "success": False,
                "method": "failed", 
                "message": "Failed to send reset link. Please try again later."
            }
    
    # Fallback to console for development (only when real email fails or isn't configured)
    if config['email_debug']:
        print("=" * 60)
        print("🔐 PASSWORD RESET EMAIL (DEVELOPMENT MODE)")
        print("=" * 60)
        print(f"📧 To: {to_email}")
        print(f"🔗 Reset Link: {reset_link}")
        print(f"🔑 Token: {reset_token}")
        print(f"⏰ Expires: 1 hour from now")
        print("=" * 60)
        print(f"🖱️  CLICK HERE: {reset_link}")
        print("=" * 60)
        print("💡 Configure SMTP_USER and SMTP_PASSWORD in .env to send real emails")
        print("=" * 60)
    
    return {
        "success": True,
        "method": "console",
        "message": "A password reset link has been sent to your email address." if not config['email_debug'] else "Reset link generated. Check console for the link (development mode)."
    }

def test_email_configuration() -> bool:
    """Test if email configuration is valid"""
    try:
        config = get_email_config()
        
        if not config['smtp_user'] or not config['smtp_password']:
            return False
            
        with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
            server.starttls()
            server.login(config['smtp_user'], config['smtp_password'])
        
        logger.info("✅ Email configuration is valid")
        return True
        
    except Exception as e:
        logger.error(f"❌ Email configuration test failed: {e}")
        return False
