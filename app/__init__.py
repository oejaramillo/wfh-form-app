import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)

# Get the DATABASE_URL, replace "postgres://" with "postgresql://" due to heroku
# database_url = os.environ.get("DATABASE_URL")
# if database_url.startswith("postgres://"):
#    database_url = database_url.replace("postgres://", "postgresql://", 1)
    
# app.config['SQLALCHEMY_DATABASE_URI'] = database_url

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'zV6XtQrUAVyL2htcmhjY'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'wfh.project.2024@gmail.com'
app.config['MAIL_PASSWORD'] = 'fxrhxouexvhvmkxs'
app.config['MAIL_DEFAULT_SENDER'] = 'wfh.project.2024@gmail.com'

mail = Mail(app)

# Set secret key from environment variable
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# For database changes and migration
migrate = Migrate(app, db)

from app import routes
