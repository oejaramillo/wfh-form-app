Work From Home (WFH) Classification App
Overview
The WFH Classification App is a web-based application designed to classify job advertisements as either suitable for working from home (WFH) or not. It allows users to review job ads and classify them, contributing to a dataset that could be used for various analytical purposes.

Architecture
The application follows a typical Flask web application structure with a front-end built using HTML, CSS, and JavaScript, and a back-end powered by Flask, a lightweight WSGI web application framework in Python.

Repository Structure
app/: Main application directory.
__init__.py: Initializes the Flask application and its configurations.
app.py: Contains the Flask application instance.
config.py: Configuration settings for the application.
models/: Contains SQLAlchemy models.
classification.py: Defines the Classification model.
classifier.py: Defines the Classifier model.
routes.py: Flask routes for handling web requests.
static/: Static files directory.
script.js: JavaScript file for front-end interactivity.
styles.css: CSS file for styling the application.
templates/: HTML templates for the application.
demo.html: Template for the demo page.
home.html: Home page template.
index.html: Main classification interface.
last.html: Final page after classification completion.
init_db.py: Script for initializing the database.
requirements.txt: List of Python dependencies for the application.
testing/: Contains tests for the application.
app_test.py, models_test.py, test_app.py: Test scripts.
Libraries and Technologies
Flask: Used for creating the web application and handling HTTP requests.
SQLAlchemy: ORM for database interactions.
SQLite: Database system used for storing data.
HTML/CSS/JavaScript: Used for building the front-end interface.
Jinja2: Templating engine for rendering HTML templates.
Purpose
The application serves as a tool for human classifiers to review and classify job advertisements based on their suitability for remote work. This classification can be valuable for studies on job market trends, especially in the context of increasing remote work opportunities.

Running the Application
Install dependencies: pip install -r requirements.txt
Initialize the database: python init_db.py
Run the application: python app/app.py