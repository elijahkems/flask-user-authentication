
from flask import Blueprint, render_template, request,  flash, redirect, session
import re

from werkzeug.utils import redirect
auth = Blueprint ("auth", __name__)
logged_user_emails = []
#validate email
def is_valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)


@auth.route("/login", methods=['GET', "POST"])
def login():
    return render_template('login.html')

@auth.route("/logout")
def logout():
    return  render_template('login.html')

@auth.route("/sign-up", methods=['GET', "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")
        # get function from global scope
        global is_valid_email
        #nothing is empty
        if email and password and confirm_password:
            if is_valid_email(email) == True:
                flash('Email is not valid', category="error")
            elif len(password) < 5:
                flash('Password is very short', category="error")
            elif password != confirm_password:
                flash("Passwords do not match", category="error")
            else:
                #store as a dictionary
                user_details = {
                    "email": email,
                    "password": password
                }
                logged_user_emails.append(user_details)
                print(logged_user_emails)
                flash("Success", category="success")
                
    return render_template('sign-up.html')

def is_valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)

