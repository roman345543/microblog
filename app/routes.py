from app import app
from flask import render_template
from app.forms import LoginFrom
from flask import flash, redirect, url_for
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html',user=user, title="Home",posts=posts)
@app.route("/login",methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in")
        return redirect(url_for("index"))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data). first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash(f"{form.username.data} sign in successfully")
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))