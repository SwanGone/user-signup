from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('sign_up.html')


@app.route("/", methods=['POST'])
def validate_login():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a username'
    elif len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Please enter a valid username (Must be between 3 and 20 characters with no spaces)'

    if password == '':
        password_error = 'Please enter a password'
    elif len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Please enter a valid password (Must be between 3 and 20 characters with no spaces'

    if verify == '':
        verify_error = 'Please verify your password'
    elif verify != password:
        verify_error = 'Your passwords do not match'

    if email == '':
        email_error = ''
    elif '@' not in email or '.' not in email or ' ' in email or len(email) < 3 or len(email) > 20:
        email_error = 'Please enter a valid email (Must contain a "." and a "@", be between 3 and 20 characters long and have no spaces)'

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/valid_login?username={0}'.format(username))
    else:
        return render_template('sign_up.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)


@app.route('/valid_login', methods=['GET'])
def valid_login():
    username = request.args.get('username')
    return render_template('valid_login.html', username=username)


app.run()