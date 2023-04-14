from app import app
from flask import render_template
from app.forms import LoginFrom
from flask import flash, redirect

@app.route('/')
@app.route('/index')
def index():
    user = { "username":'Roman' }
    posts = [
        {
            'author' : {'username': 'Mark Then'},
            'body': 'Люблю математику'
        },
        {
            'author': {'username': 'Mark Tven'},
            'body': 'учусь блин '
        },
        {
            'author': {'username': 'Big Ben'},
            'body': 'товарищ андрей'
        }
    ]
    return render_template('index.html',user=user,posts=posts)
@app.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)