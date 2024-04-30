
from .. import db

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    results = db.Column(db.Integer, nullable=False)
    commands = db.Column(db.String(255))
    timestamp=db.Column(db.DateTime, server_default=db.func.now())
    duration = db.Column(db.Numeric(20,6), nullable=False)