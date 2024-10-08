from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import InputRequired, Length, EqualTo, Email
from flask_wtf.file import FileRequired, FileAllowed
#from email_validator import validate_email, EmailNotValidError

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired(), Length(min=2, max=40)])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Destination Image', validators=[FileRequired(message='The countries image is required!'), FileAllowed(['jpg', 'png', 'jpeg', "JPG", "PNG", "JPEG"])])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField('Submit Destination', render_kw={'class': 'btn btn-primary btn-lg px-5'})

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Create')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Please enter your username")])
    password = PasswordField('Password', validators=[InputRequired("Please enter your password")])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Please enter your username")])
    email = StringField('Email', validators=[InputRequired("Please enter your email address"), Email()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])
    submit = SubmitField('Register')