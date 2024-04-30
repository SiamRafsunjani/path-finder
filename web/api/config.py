
import os

class Config:
    FLASK_APP=os.environ.get('FLASK_APP') or 'api/__init__.py'
    FLASK_ENV="production"
    FLASK_DEBUG=1
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False