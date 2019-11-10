from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = '24944d6d0064003ab376ed5a113cebc8'


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
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/test")
def test():
    return render_template('test.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
