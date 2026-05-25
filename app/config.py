import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-fallback-secret-key'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///bionic_pancreas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Simulation Parameters
    CARB_FACTOR = float(os.environ.get('CARB_FACTOR', 4.0))
    INSULIN_FACTOR = float(os.environ.get('INSULIN_FACTOR', 40.0))
    EXERCISE_FACTOR = float(os.environ.get('EXERCISE_FACTOR', 20.0))

    GLUCOSE_INITIAL = int(os.environ.get('GLUCOSE_INITIAL', 100))
    GLUCOSE_LOW = int(os.environ.get('GLUCOSE_LOW', 70))
    GLUCOSE_HIGH = int(os.environ.get('GLUCOSE_HIGH', 180))

    # Telegram Bot
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

    # Upload configuration
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(basedir, 'static/uploads')

    # Localization
    LANGUAGES = ['tr', 'en']
