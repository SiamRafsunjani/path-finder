
import os

class Config:
    FLASK_APP=os.environ.get('FLASK_APP') or 'api/__init__.py'
    FLASK_ENV="development"
    FLASK_DEBUG=1
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST')}:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}"    
    SQLALCHEMY_TRACK_MODIFICATIONS = False