from flask import Blueprint, render_template, request, flash
from . models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template('home.html')


@auth.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/sign-up', methods=["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('Too short email, it has to be min 4 chars', category='error')
        elif len(first_name) < 5:
            flash('Too short Firstname, it has to be min 4 chars', category='error')
        elif len(password1) < 4:
            flash('Password len too short', category='error')
        elif password1 != password2:
            flash('Password mismatch', category='error')
        else:
            new_user = User(email = email,
                            first_name = first_name,
                            password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Yay, welcome to Notebook! You are registered', category='Success')
    return render_template('sign_up.html')
