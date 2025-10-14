# 📧 IntelliGrade Email Setup Guide

## 🎯 Quick Setup for Real Email Sending

Your forgot password feature is now **fully functional** but currently shows reset links in the console. To send **real emails**, follow these simple steps:

### 🚀 Option 1: Automated Setup (Recommended)

```bash
cd backend
python setup_email.py
```

This interactive script will guide you through:
- Email provider selection (Gmail, Outlook, Yahoo, Custom)
- Credential input with security tips
- Automatic .env file creation
- Configuration testing

### 🛠️ Option 2: Manual Setup

1. **Create `.env` file** in the `backend` folder:

```env
# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your.email@gmail.com
SMTP_PASSWORD=your_app_password_here
FROM_NAME=IntelliGrade Support
FRONTEND_URL=http://localhost:5174
```

2. **For Gmail (Recommended):**
   - Enable 2-Factor Authentication
   - Go to [Google Account Settings](https://myaccount.google.com/)
   - Security → 2-Step Verification → App passwords
   - Generate password for "IntelliGrade"
   - Use this 16-character password (not your regular password)

3. **For Other Providers:**
   - **Outlook:** `smtp-mail.outlook.com:587`
   - **Yahoo:** `smtp.mail.yahoo.com:587`
   - **Custom:** Use your provider's SMTP settings

### 🧪 Testing Your Setup

1. **Check Status:**
   ```
   GET http://localhost:8000/auth/email-status
   ```

2. **Test Forgot Password:**
   - Go to your forgot password page
   - Enter any email address
   - Check if real email is sent or console fallback is used

### 🔄 How It Works Now

1. **Without Email Config:** Shows reset link in console (current behavior)
2. **With Email Config:** Sends professional HTML emails with reset links
3. **Email Fails:** Automatically falls back to console display

### 📧 Email Template Features

When properly configured, users receive beautiful HTML emails with:
- ✅ Professional IntelliGrade branding
- ✅ Secure one-click reset buttons
- ✅ 1-hour expiration warnings
- ✅ Security notices
- ✅ Mobile-friendly design
- ✅ Fallback text version

### 🔐 Security Features

- Reset tokens expire in 1 hour
- Tokens are cryptographically secure (32 bytes)
- One-time use only
- Email validation
- Rate limiting protection

### 📱 Production Deployment

For production, set these environment variables:
```env
SMTP_SERVER=your.smtp.server
SMTP_PORT=587
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your_secure_password
FROM_NAME=IntelliGrade Support
FRONTEND_URL=https://yourdomain.com
```

### 🎉 What's Working Right Now

- ✅ Beautiful forgot password page
- ✅ Smart email system (real email → console fallback)
- ✅ Professional email templates
- ✅ Development helper tools
- ✅ Reset password functionality
- ✅ Security best practices
- ✅ Error handling and logging

### 🚨 Important Notes

1. **Gmail Users:** Must use App Passwords (not regular password)
2. **Environment Variables:** Restart server after changing .env
3. **Security:** Never commit real credentials to version control
4. **Development:** Console fallback works perfectly for testing

### 🎯 Ready to Go Live?

Your system is **production-ready**! Just:
1. Set up real SMTP credentials
2. Update FRONTEND_URL to your domain
3. Deploy and enjoy real-time password resets! 🎉

---

**Need Help?** 
- Run `python backend/setup_email.py` for guided setup
- Check `http://localhost:8000/auth/email-status` for current status
- Email functionality works seamlessly in both development and production!