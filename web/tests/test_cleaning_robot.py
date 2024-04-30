import unittest
from api.cleaning_robot.calculate_path import RobotStepCounter

"""
Unit tests for the CleaningRobotStepCounter class
"""
class CleaningRobotStepCounterTest(unittest.TestCase):
    
    """
    Starting at 0,0 and moving 5 steps north
    The robot should visit 6 unique points
    """
    def test_unique_points_visited_count(self):
        start = {'x': 0, 'y': 0}
        commands = [{
            "direction": 'north',
            "steps": 5
        }]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 6

    """
    Test the unique points visited when the robot moves in a single direction
    """
    def test_unique_points_visited_in_single_direction(self):
        start = {'x': 0, 'y': 0}
        commands = [{
            "direction": 'north',
            "steps": 1
        }, {
            "direction": 'north',
            "steps": 2
        }, 
        {
            "direction": 'north',
            "steps": 3
        }]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 7

    """
    Starting at 0,0 and moving no steps with no commands
    The robot should visit 1 unique point
    """
    def test_unique_points_without_any_commands(self):
        start = {'x': 0, 'y': 0}
        commands = []
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 1

    """
    Starting from point other than origin
    """
    def test_unique_points_other_than_origin(self):
        start = {'x': 10, 'y': 22}
        commands = [
            {
                "direction": "east",
                "steps": 2 
            },
            {
                "direction": "north",
                "steps": 1
            }
        ]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 4


    """
    Starting from point other than origin
    """
    def test_unique_points_in_negative_direction(self):
        start = {'x': -10, 'y': -22}
        commands = [
            {
                "direction": "east",
                "steps": 5
            },
            {
                "direction": "north",
                "steps": 2
            }
        ]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 8


    """
    Checks the unique points when the robot moves to the same point 
    multiple times
    """
    def test_unique_points_for_diagonal_movement(self):
        start = {'x': 0, 'y': 0}
        commands = [
            {
                "direction": "north",
                "steps": 5
            },
            {
                "direction": "south",
                "steps": 5
            },
            {
                "direction": "east",
                "steps": 5
            },
            {
                "direction": "west",
                "steps": 5
            }
        ]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 11


    """
    Checks the unique points when the robot gets repeated commands
    """
    def test_unique_points_for_repeated_commands(self):
        start = {'x': 0, 'y': 0}
        commands = [
            {
                "direction": "north",
                "steps": 5
            },
            {
                "direction": "south",
                "steps": 5
            },
            {
                "direction": "east",
                "steps": 5
            },
            {
                "direction": "west",
                "steps": 5
            }
        ]
        
        # Repeat the commands 3 times
        commands = commands * 3
        
        step_counter = RobotStepCounter(
            start=start,
            commands=commands 
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 11


    """
    Checks the unique points with complex movements
    """
    def test_unique_points_for_complex_commands(self):
        start = {'x': 0, 'y': 0}
        commands = [
            {
                "direction": "north",
                "steps": 5
            },
            {
                "direction": "west",
                "steps": 2
            },
            {
                "direction": "east",
                "steps": 5
            },
            {
                "direction": "south",
                "steps": 50
            },
            {
                "direction": "west",
                "steps": 50
            }
        ]
        step_counter = RobotStepCounter(
            start=start,
            commands=commands 
        )
        
        result = step_counter.calculate()
        assert result['unique_points_visited'] == 111


if __name__ == "__main__":
    unittest.main()