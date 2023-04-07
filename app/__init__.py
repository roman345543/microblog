from flask import Flask
from config import Config
from flask_sqlalchemy import SQLALchemy
from flask_nigrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLALchemy(app)
nigrate = Migrate


from app import routes