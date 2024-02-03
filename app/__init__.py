import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gdzejgzevtbjsp:ee962f1c535b3105ed8d43927dc95042fe8573323daa1807ca4c543e0b2d5003@ec2-44-218-92-155.compute-1.amazonaws.com:5432/d45l560lrs55ad'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set secret key from environment variable
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# For database changes and migration
migrate = Migrate(app, db)

from app import routes
