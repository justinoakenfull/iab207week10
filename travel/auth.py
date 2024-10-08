from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from .models import User
from . import db

authBlueprint = Blueprint('auth', __name__)

@authBlueprint.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        flash(f'Login requested for user {loginForm.username.data}', 'success')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=loginForm, heading="Login")

@authBlueprint.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        flash(f'Account created for {registerForm.username.data}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=registerForm, heading="Register")

@authBlueprint.route('/logout')
def logout():
    return redirect(url_for('main.home'))