import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')