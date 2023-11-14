from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Change this to your database URI

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Set login view for unauthorized users
    login_manager.login_view = 'login'

    # Import and register blueprints
    from app import routes
    app.register_blueprint(routes.bp)

    return app
