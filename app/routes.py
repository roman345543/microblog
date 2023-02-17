from app import app
from flask import render_templates


@app.route('/')
@app.route('/index')
def index():
    user = { "username":'Roman' }
    return render_templates('index.html',title='Home',user=user)
