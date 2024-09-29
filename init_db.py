from app import db, app  # Import the db instance and app instance

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    init_db()
