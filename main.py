from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='login')

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == os.environ.get("EMAIL") and form.password.data == os.environ.get("PASSWORD"):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
