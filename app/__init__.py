from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
babel = Babel()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models  # noqa: F401 — ensures tables are visible to Flask-Migrate
    login.init_app(app)
    login.login_view = 'auth.login'
    login.login_message_category = 'info'
    babel.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.simulation import bp as simulation_bp
    app.register_blueprint(simulation_bp, url_prefix='/simulation')

    from app.meals import bp as meals_bp
    app.register_blueprint(meals_bp, url_prefix='/meals')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp) # url_prefix='/api/v1' is set in api/__init__.py

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
