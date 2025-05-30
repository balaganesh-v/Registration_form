from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret')

users = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash("All fields are required!", "error")
            return render_template('register.html')

        users.append({'username': username, 'email': email})
        flash("Registration successful!", "success")
        return redirect(url_for('success', username=username))

    return render_template('register.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
