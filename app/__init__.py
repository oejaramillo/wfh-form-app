import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vcvcjaecvjtmzs:4b1e1cd1f29058cf3f6d7214e689a3cc06709c3d7725d64e20f2bbe712494479@ec2-54-234-13-16.compute-1.amazonaws.com:5432/d2h0bn6k19adl1'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set secret key from environment variable
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# For database changes and migration
migrate = Migrate(app, db)

from app import routes
