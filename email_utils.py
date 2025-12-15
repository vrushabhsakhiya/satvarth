# email_utils.py

from flask_mail import Message

def send_contact_email(mail, recipient, data):
    try:
        msg = Message(
            subject=f"Contact Form: {data.get('subject', 'New Inquiry')}",
            sender=mail.default_sender,          # 🔴 REQUIRED
            recipients=[recipient],
            reply_to=data.get('email')           # 🔴 REQUIRED
        )

        msg.body = f"""
New Contact Form Submission
---------------------------
Name: {data.get('name')}
Email: {data.get('email')}
Phone: {data.get('phone')}
Subject: {data.get('subject')}

Message:
{data.get('message')}
"""

        mail.send(msg)

        return {
            'success': True,
            'message': 'Thank you! Your message has been sent successfully.'
        }

    except Exception as e:
        print("CONTACT EMAIL ERROR:", e)
        return {
            'success': False,
            'message': 'Email sending failed. Please try again later.'
        }
