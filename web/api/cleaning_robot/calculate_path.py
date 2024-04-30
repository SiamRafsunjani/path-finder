"""
This module is responsible for calculating the path of the 
cleaning robot and the number of unique points visited

Robot can move in 4 directions: north, south, east, west
Robot can move multiple steps in a single direction

Class parameters: start, commands
start: dict - the starting point of the robot {x: int, y: int}
commands: list - list of commands for the robot to move in the grid
    commands: dict - {direction: str, steps: int}
"""
class RobotStepCounter:
    def __init__(self, start: dict, commands: list):
        self.current_point = start
        
        # Convert the x and y coordinates to integers
        self.current_point['x'] = int(self.current_point['x'])
        self.current_point['y'] = int(self.current_point['y'])
        
        self.commands = commands
        """
        Initiate the step counter to 1
        as the robot is already at the start position
        """
        self.unique_points_visited = 1
        
        """
        Map for the points that the robot has visited
        The first point is the start point
        """        
        self.visited_points = {(start['x'], start['y'])}

    """
    Move the robot based on the direction and steps
    """    
    def move_robot(self, command):
        direction = command['direction']
        steps = int(command['steps'])
        
        # Move the robot in the direction 
        # with the number of steps
        while steps > 0:
            if direction == 'north':
                self.current_point['y'] += 1
            elif direction == 'south':
                self.current_point['y'] -= 1
            elif direction == 'east':
                self.current_point['x'] += 1
            elif direction == 'west':
                self.current_point['x'] -= 1
            
            """
            Check if the point is already visited
            """
            if (self.current_point['x'], self.current_point['y']) not in self.visited_points:
                self.unique_points_visited += 1
                self.visited_points.add((self.current_point['x'], self.current_point['y']))

            # Complete the step
            steps -= 1
    
    def calculate(self):
        for command in self.commands:
            self.move_robot(command)
            
        return { 
            'unique_points_visited': self.unique_points_visited, 
            'path': list(self.visited_points) 
        }