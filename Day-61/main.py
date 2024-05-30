from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import secrets


class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
