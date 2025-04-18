from app import app, db
from models import Trade  # Import all your models

with app.app_context():
    db.create_all()  # This creates all tables
