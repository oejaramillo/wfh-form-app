from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
# Ensure you have the correct path for your SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Oscar Local\wfh-form-app\data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with Flask app
db = SQLAlchemy(app)

# Import models after initializing db to avoid circular imports
from app.models.classifier import Classifier
from app.models.classification import Classification

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()

if __name__ == '__main__':
    init_db()
    print("Current working directory:", os.getcwd())
