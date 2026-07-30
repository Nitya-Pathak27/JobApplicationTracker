from flask import session, flash, redirect, url_for
from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from __init__ import app, mail
from flask_mail import Message

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please login first to access this page...", "error")
            return redirect(url_for('login_page'))
        
        return function(*args, **kwargs)
    return wrapper

# Generate reset token
def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(app.secret_key)
    token = serializer.dumps(email)
    return token

# Send reset email
def send_reset_email(user_email):
    token = generate_reset_token(user_email)
    reset_link = f"http://127.0.0.1:5000/reset-password/{token}"

    message = Message(
        subject = "Password Reset Request",
        sender = app.config['MAIL_USERNAME'],
        recipients = [user_email],
    )

    message.body = f"""
Hello,

Click the link below to reset your password:

{reset_link}

If you did not request this, ignore this email.
"""
    mail.send(message)

# Verify reset token
def verify_reset_token(token):
    serializer = URLSafeTimedSerializer(app.secret_key)
    try:
        email = serializer.loads(token, max_age = 300)
        return email
    except:
        return None