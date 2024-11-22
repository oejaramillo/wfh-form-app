from app import db, app  # Import the db instance and app instance

def init_db():
    with app.app_context():
        db.drop_all()  # Drops all tables
        db.create_all()  # Creates all tables

# Directly run the function when the script is executed
init_db()