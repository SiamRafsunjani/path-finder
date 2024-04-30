from flask_smorest import Blueprint
from flask import request, jsonify, current_app as app
from pydantic import ValidationError
import datetime

from ..common.utils.exceptions import InvalidPayloadException, ValidationException
from ..validation.core import RobotStepCalculationValidator
from .calculate_path import RobotStepCounter
from .. import db
from ..models.results import Results

cleaning_robot_blueprint = Blueprint(
    'cleaning_robot', 'cleaning_robot', 
    description='Handles the cleaning robot functionality', 
    url_prefix='/tibber-developer-test'
)

"""
Calculated the cleaning steps taken by the robot and stores the data in the database
"""
@cleaning_robot_blueprint.route('/enter-path', methods=['POST'])
def calculate_steps():
    post_data = {**request.get_json()}
    if not post_data:
        raise InvalidPayloadException('No input data provided')
    
    try:
        # Basic validation of the input data
        RobotStepCalculationValidator(**post_data)
    except ValidationError as e:
        app.logger.error(f'Error validating input data: {str(e)}')
        raise InvalidPayloadException('Invalid input data provided, start point and commands are required')

    start_time = datetime.datetime.now()
    robot_step_counter = RobotStepCounter(**post_data)
    counted_steps = robot_step_counter.calculate()
    execution_time = datetime.datetime.now() - start_time
    
    # log the results
    app.logger.info({
        "message": "steps counted", 
        "steps": counted_steps['unique_points_visited'], 
        "execution_time": f'{execution_time.microseconds} microseconds' 
    })

    # Store the data in the results table
    # Todo: Potentially move this to a service. but now it's fine
    try:
        results = Results(
            results=counted_steps['unique_points_visited'], 
            commands=len(post_data['commands']), 
            duration=execution_time.microseconds / 1000000 # convert to seconds
        )
        db.session.add(results)
        # Note: flush is used to get the id of the inserted row
        # Todo: Check the SQLAlchemy documentation for potential issues with using flush
        db.session.flush()
        db.session.commit()
    except Exception as e:
        app.logger.error(f'Error storing results in the database: {str(e)}')
        raise ValidationException('Error storing results in the database')
    
    return jsonify(
        id=results.id, success=True, unique_points_visited=counted_steps['unique_points_visited'],
        commands_executed=len(post_data['commands']), execution_time="{:.6f}".format(execution_time.microseconds / 1000000)
    )
