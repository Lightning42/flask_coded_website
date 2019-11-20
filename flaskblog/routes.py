from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Username',
        'title': 'Topbar Navigation Test',
        'content': 'Currently not functional',
        'date_posted': 'Novemeber 4th 2019'
    },
    {
        'author': 'Username',
        'title': 'Shortcut Bar Test',
        'content': 'Currently not functional',
        'date_posted': 'Novemeber 4th 2019'
    },
    {
        'author': 'Username',
        'title': 'Profile Connection Test',
        'content': 'Currently not functional',
        'date_posted': 'Novemeber 4th 2019'
    },
    {
        'author': 'Username',
        'title': 'DataBase Test',
        'content': 'Currently not functional',
        'date_posted': 'Novemeber 4th 2019'
    },
    {
        'author': 'Username',
        'title': 'First Post!',
        'content': 'This is the first post on this python coded website.',
        'date_posted': 'Novemeber 3rd 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/test")
def test():
    return render_template('dropdown.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You have already logged in!', 'danger')
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You have already logged in!', 'danger')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('home'))


@app.route("/settings")
@login_required
def settings():
    return render_template('settings.html', title='Account Settings')
