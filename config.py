import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or '34554367#_roman'
    