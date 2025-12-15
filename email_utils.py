import threading
from flask_mail import Message

def send_async_email(app, mail, msg):
    with app.app_context():
        mail.send(msg)

def send_contact_email(app, mail, recipient, data):
    try:
        msg = Message(
            subject=f"Contact Form: {data.get('subject', 'New Inquiry')}",
            sender=mail.default_sender,
            recipients=[recipient],
            reply_to=data.get('email')
        )

        msg.body = f"""
Name: {data.get('name')}
Email: {data.get('email')}
Phone: {data.get('phone')}
Message:
{data.get('message')}
"""

        thread = threading.Thread(
            target=send_async_email,
            args=(app, mail, msg)
        )
        thread.start()

        return {'success': True, 'message': 'Message sent successfully.'}

    except Exception as e:
        return {'success': False, 'message': str(e)}
