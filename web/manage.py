from flask.cli import FlaskGroup
from api import app, db
import click
import unittest
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

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()
