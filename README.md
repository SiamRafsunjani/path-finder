# Path Finder

A microservice that calculates the path of a cleaning robot and persists in database. The path of the robot's movement is described by the starting coordinates and move commands. After the cleaning has been done, the robot reports the number of unique places cleaned. This service stores the results into the database and return the created record in JSON format.

#### Functional requirements are.

1. A ```POST``` endpoint ```/tibber-developer-test/enter-path```
2. The starting point is as follows
```(x, y) : −100 000 ≤ x ≤ 100 000, x ∈ Z −100 000 ≤ y ≤ 100 000, y ∈ Z```
3. Number of commands can be ```0 ≤ number of commands elements ≤ 10000```
4. Returns the number of unique points visited by the robot and number of commands executed with it's execution time.


#### Tech Stack:

 - **Web framework:** Flask
 - **ORM:** SQLAlchemy
 - **Database:** PostgresSQL
 - **Parsing/Validation:** Pydantic
 - **Containerization:** Docker





## Get Started

#### Folder structure

```
- web
    - api
        - cleaning_robot: the core functionality resides here
        - common: the error handler is here now. could be extended later for other common functionalities
        - models: the database models are here. Currently only one model is here. The Result persist model
        - validation: the validation schema is here. The Pydantic schema is here
        __init__.py: the app is created here
        - config.py: the configuration file is here
    - tests: the test cases are here
    - docs: the Architecture design records (ADR) are here. The ADRs are written in markdown format and are stored here. We can add swagger documentation here as well
    - requirements.txt: the dependencies are here
    - Dockerfile
    - docker-compose.yml
```



#### Requirements

* Docker
* Docker Compose
* Docker Machine
* Other dependencies are listed in `requirements.txt` and are installed automatically.

Get docker: https://docs.docker.com/get-docker/

Clone all the project from this repository and move to repository folder.

Rename `.env.example` file to `.env.dev`. It is located in ```web/api/``` folder. All environment variables are set from this file.

Make sure you set the following environment variables:

    FLASK_APP
    FLASK_ENV
    FLASK_DEBUG
    DATABASE_URL



Build the images and run the containers.
```bash
docker-compose up --build
```

or if you want to run it in detached (background) mode:
```bash
docker-compose up -d --build
```
Make sure all containers are running:
```bash
docker-compose ps
```
```bash                                                                       
web
db                                                      
```

Then create all development db tables:

```docker
docker-compose exec web python manage.py create_db
```

This will run the flask app in development mode. You can access the app at http://localhost:5000. Also you can develop the app in this mode with hot reload enabled.

## API Documentation
```
POST /tibber-developer-test/enter-path
Authentication: None

Request Body:
{
    "start": {
        "x": 0,
        "y": 0
    },
    "commands": [
        {
            "direction": "north",
            "steps": 1
        },
        {
            "direction": "east",
            "steps": 1
        }
    ]
}

Sample Response:
Status Code: 200
{
    "id": 1,
    "unique_points_visited": 3,
    "commands_executed": 2,
    "execution_time": 0.000
}

Sample Error Response:
Status Code: 400
{
    "message": "Invalid request body"
    "status_code": 400
}
```


## Testing and Coverage

Run tests using:
```docker
docker-compose exec web python manage.py test
```
You should see an output like this:
```bash

test_unique_points_for_complex_commands (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_for_diagonal_movement (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_for_repeated_commands (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_in_negative_direction (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_other_than_origin (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_visited_count (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_visited_in_single_direction (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok
test_unique_points_without_any_commands (test_cleaning_robot.CleaningRobotStepCounterTest) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

## Future improvements

1. Make the application production ready with server setup with nginx and gunicorn. 
2. Add docker-compose file for production.
3. Add integration tests.
4. Add more validation checks and error handling. For this exercise we have only added the basic validation checks.
5. Add more logging and monitoring.
6. Improve the database connection handling to have proper connection pooling.
7. Check the performance of the application with large number of requests.
8. Add more test cases to cover all the edge cases for example if the robot moves out of the grid, etc.
9. Design the error handling in a better way. success and error response should be consistent.
