from flask.cli import FlaskGroup
from api import app, db
import click
import unittest
import os
cli = FlaskGroup(app)

@cli.command()
@click.argument('file', required=False)
def test(file):
    """
    Run the tests without code coverage
    """
    pattern = 'test_*.py' if file is None else file
    tests = unittest.TestLoader().discover('tests', pattern=pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

"""
Ticket: Create a new command to create the database tables
Have more checks so that the database is not created in production
Check the DB url and everything before creating the database so 
accidental pointing to prod does not end everyone's sleep
"""
@cli.command("create_db")
def create_db():
    if os.environ.get('FLASK_ENV') == 'production':
        raise ValueError("Cannot create database in production environment")
    else:
        db.drop_all()
        db.create_all()
        db.session.commit()

if __name__ == "__main__":
    cli()
