# Work From Home (WFH) Classification App

## Overview

The WFH Classification App is a web-based application designed to classify job advertisements as either suitable for working from home (WFH) or not. It allows users to review job ads and classify them, contributing to a dataset that could be used for various analytical purposes. This app was developed as part of the Project “Remote Work, Wages, and Competition: Disentangling demand and supply influences.”

## Architecture

The application follows a typical Flask web application structure with a front-end built using HTML, CSS, and JavaScript, and a back-end powered by Flask, a lightweight WSGI web application framework in Python.

### Repository Structure

- `app/`: Main application directory.
  - `__init__.py`: Initializes the Flask application and its configurations.
  - `app.py`: Contains the Flask application instance.
  - `config.py`: Configuration settings for the application.
  - `models.py`: Contains SQLAlchemy models.
    - `classification`: Defines the Classification model for storing the actual classification decision of human classifiers.
    - `classifier`: Defines the Classifier model for storing data from the human classifers and mapping their classification
  - `routes.py`: Flask routes for handling web requests.
  - `static/`: Static files directory.
    - `script.js`: JavaScript file for front-end interactivity and server comunication with **AJAX** framework 
    - `styles.css`: CSS file for styling the application.
  - `templates/`: HTML templates for the application.
    - `inicio.html`: Home page template. 
    - `datos_demo.html`: Template for the demographic form.
    - `wfh_classification.html`: Main classification interface.
    - `last.html`: Final page after classification completion.
- `init_db.py`: Script for initializing the database.
- `requirements.txt`: List of Python dependencies for the application.

### Libraries and Technologies

- **Flask**: Used for creating the web application and handling HTTP requests.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database system used for storing data.
- **HTML/CSS/JavaScript**: Used for building the front-end interface.
- **Jinja2**: Templating engine for rendering HTML templates.

## Purpose

The application serves as a tool for human classifiers to review and classify job advertisements based on their suitability for remote work. This classification can be valuable for studies on job market trends, especially in the context of increasing remote work opportunities.

## Running the Application

1. Install dependencies: `pip install -r requirements.txt`
2. Initialize the database: `python init_db.py`
3. Run the application: `python run.py`
