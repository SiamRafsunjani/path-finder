
from flask import Flask
from dotenv import load_dotenv

# load environment variables into flask config
load_dotenv()
from .config import Config

from werkzeug.exceptions import HTTPException 
import logging
from flask_sqlalchemy import SQLAlchemy
from pythonjsonlogger import jsonlogger
from flask_migrate import Migrate
from .common.utils import exceptions, errors

"""
Ticket: Implement a config file to store all the environment variables
"""

app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the database 
db = SQLAlchemy()
migrate = Migrate(app, db)

"""
Ticket: Extend this logger to log to files and format the logs
add more metadata to the logs ie. user_id, request_id, function name etc
Currently the logger logs to the console and formats the logs as JSON
"""
logger = logging.getLogger()

def register_error_handlers(app):
    # register error handlers
    app.register_error_handler(exceptions.InvalidPayloadException, errors.handle_exception)
    app.register_error_handler(exceptions.BadRequestException, errors.handle_exception)
    app.register_error_handler(exceptions.UnauthorizedException, errors.handle_exception)
    app.register_error_handler(exceptions.ForbiddenException, errors.handle_exception)
    app.register_error_handler(exceptions.NotFoundException, errors.handle_exception)
    app.register_error_handler(exceptions.ServerErrorException, errors.handle_exception)

    # Werkzeug global exceptions
    app.register_error_handler(Exception, errors.handle_general_exception)
    app.register_error_handler(HTTPException, errors.handle_werkzeug_exception)
    
    return app

def create_app():
    
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(timestamp=True)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

    db.init_app(app)

    from .cleaning_robot import cleaning_robot_blueprint    
    app.register_blueprint(cleaning_robot_blueprint)
    register_error_handlers(app)
    
    return app

app = create_app()
