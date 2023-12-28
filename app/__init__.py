from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = "\xc1}\xf7F\xfdd'\x0f\x7f\x85i\xe2C\xa0\n\xf1"  # Set a strong, random key

from app import routes
