from flask import Flask
from models import db
import os
from routes import register_routes


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trades.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize database
    db.init_app(app)

    # Register routes
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)