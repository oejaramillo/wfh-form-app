import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Get the DATABASE_URL, replace "postgres://" with "postgresql://" due to heroku
database_url = os.environ.get("DATABASE_URL")
if database_url.startswith("postgres://"):
   database_url = database_url.replace("postgres://", "postgresql://", 1)
    
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set secret key from environment variable
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# For database changes and migration
migrate = Migrate(app, db)

from app import routes
