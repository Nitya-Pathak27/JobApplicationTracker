from __init__ import app
from werkzeug.security import generate_password_hash, check_password_hash
from db import db, cursor
from database.user_queries import (
    create_user, fetch_user_by_email, update_user_password
)
from utils import (send_reset_email, verify_reset_token)
from flask import render_template, request, redirect, session, url_for, flash

# register route
@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        name = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not name or not email or not password or not confirm_password:
            flash("Please fill in all the fields...", "error")
            return redirect(url_for('register_page'))

        if password != confirm_password:
            flash("Passwords do not match. Please try again...", "error")
            return redirect(url_for('register_page'))
        
        existing_user = fetch_user_by_email(email)
        if existing_user:
            flash("Email already registered...", "error")
            return redirect(url_for('register_page'))

        hashed_password = generate_password_hash(password)
        create_user(name, email, hashed_password)

        flash("Registration successful! Please login...", "success")
        return redirect(url_for('login_page'))
    
    return render_template("register.html")

# login route
@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Please fill in all the fields...", "error")
            return redirect(url_for('login_page'))
        
        user = fetch_user_by_email(email)

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            flash("Login successfully...", "success")
            return redirect(url_for('home_page'))
        else:
            flash("Invalid email or password. Please try again...", "error")
            return redirect(url_for('login_page'))
        
    return render_template("login.html")

# forgot password route
@app.route('/forgot-password', methods = ['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')

        if not email:
            flash("Please enter your registered email address...", "error")
            return redirect(url_for('forgot_password'))
        
        # Check user exits
        user = fetch_user_by_email(email)
        if not user:
            flash("No account found with this email address..", "error")
            return redirect(url_for('register_page'))
        
        # send reset email
        send_reset_email(email)
        flash("Password reset link sent to your email. Please check your inbox...", "success")
        return redirect(url_for('check_email'))

    return render_template("forgot_pwd.html")

# check email route
@app.route('/check-email')
def check_email():
    return render_template("check_email.html")

# reset password route
@app.route('/reset-password/<token>', methods = ['GET', 'POST'])
def reset_password(token):
    email = verify_reset_token(token)

    if not email:
        flash("Invalid or expired token. Please try again...", "error")
        return redirect(url_for('forget_password'))
    
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if not new_password or not confirm_password:
            flash("Please fill in all the fields...", "error")
            return redirect(url_for('reset_password', token=token))
        
        if new_password != confirm_password:
            flash("Password mismatch. Please try again...", "error")
            return redirect(url_for('reset_password', token=token))
        
        hashed_password = generate_password_hash(new_password)
        update_user_password(email, hashed_password)

        flash("Your password has been reset successfully. Please login...", "success")
        return redirect(url_for('login_page'))

    return render_template("reset.html", token=token)

# logout route
@app.route('/logout')
def logout_page():
    session.clear()
    flash("You have been logged out successfully...", "success")
    return redirect(url_for('login_page'))
