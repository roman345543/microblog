from app import app
from flask import render_template


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
