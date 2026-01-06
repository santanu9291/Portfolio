# Contact Form Email Setup Guide

Your contact form is now configured to send REAL emails using FormSubmit.co (free service).

## 🚀 Quick Setup (2 minutes)

### Step 1: Add Your Email
1. Open `index.html`
2. Find this line (around line 239):
   ```html
   <form id="contactForm" class="contact-form" action="https://formsubmit.co/your-email@example.com" method="POST">
   ```
3. Replace `your-email@example.com` with YOUR REAL EMAIL ADDRESS

### Step 2: Verify Your Email (First Time Only)
1. Open your portfolio in a browser
2. Submit a test message through the contact form
3. Check your email inbox
4. **Click the verification link** from FormSubmit
5. Done! Now all future messages will come directly to your email

### Step 3: Update Your Contact Information
In `index.html`, update your real contact details:
```html
<li>
  <span class="contact-icon">📧</span>
  your-real-email@gmail.com  <!-- Change this -->
</li>
<li>
  <span class="contact-icon">🌐</span>
  www.yourwebsite.com  <!-- Change this -->
</li>
<li>
  <span class="contact-icon">📱</span>
  +91-XXXXXXXXXX  <!-- Change this -->
</li>
```

## ✅ What You'll Receive

When someone submits the form, you'll get an email with:
- Sender's name
- Sender's email (you can reply directly)
- Their message
- Timestamp

## 🎨 Features Included

✓ Spam protection (honeypot field)
✓ No CAPTCHA needed
✓ Professional email template
✓ Custom subject line: "New Portfolio Contact Message!"
✓ Free forever (unlimited submissions)
✓ No signup required

## 🔧 Alternative Options

### Option 2: EmailJS (More Control)
If you want more customization:
1. Sign up at https://emailjs.com (free tier: 200 emails/month)
2. Get your Service ID, Template ID, and Public Key
3. Replace FormSubmit code with EmailJS integration

### Option 3: Your Own Backend
If you have a server:
1. Create a PHP/Node.js email endpoint
2. Update form action to your server URL
3. Handle email sending on your backend

## 📧 Email Template

The emails you receive will look like this:

```
From: FormSubmit <noreply@formsubmit.co>
Subject: New Portfolio Contact Message!

Name: John Doe
Email: john@example.com
Message: Hi, I'm interested in working with you...
```

## 🛡️ Security Features

- **Honeypot field**: Blocks bots (hidden `_honey` field)
- **No database**: Messages go straight to your email
- **HTTPS**: All submissions are encrypted
- **Spam filtering**: FormSubmit has built-in protection

## 🐛 Troubleshooting

### Emails not arriving?
1. Check your spam/junk folder
2. Make sure you clicked the verification link
3. Verify your email address in the form action is correct
4. Wait 1-2 minutes (sometimes delayed)

### Form not submitting?
1. Check browser console for errors (F12)
2. Make sure all fields are filled
3. Check internet connection
4. Try a different browser

### Want to customize?
Add these hidden fields to the form:

```html
<!-- Redirect after submission -->
<input type="hidden" name="_next" value="https://yourwebsite.com/thank-you.html">

<!-- Change reply-to address -->
<input type="hidden" name="_replyto" value="custom-reply@example.com">

<!-- CC yourself -->
<input type="hidden" name="_cc" value="backup@example.com">
```

## 📱 Test Your Setup

1. Open your portfolio
2. Fill out the contact form
3. Submit
4. Check your email inbox (and spam folder)
5. You should receive the message within 1-2 minutes

**First submission requires email verification!**

---

**Need help?** Check FormSubmit documentation: https://formsubmit.co

Your contact form is now fully functional! 🎉
