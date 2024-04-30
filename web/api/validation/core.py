from pydantic import BaseModel

"""
Validation for the input data of the robot step calculation.
only validates if the fields are present 
Scope mentioned in the ticket
1. The data is already cleaned and validated before it reaches this function
2. The robot will not go outside of the grid/room
"""
class RobotStepCalculationValidator(BaseModel):
    start: dict
    commands: list