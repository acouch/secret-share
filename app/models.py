from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Secret(db.Model):
    secret_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    confidante = db.Column(db.String)
    message = db.Column(db.String, unique=True, nullable=False)
    hash = db.Column(db.String)    
