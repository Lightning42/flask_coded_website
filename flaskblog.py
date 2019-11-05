from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login")
def login():
    return render_template('login.html', title='Login')


@app.route("/test")
def test():
    return render_template('test.html')
