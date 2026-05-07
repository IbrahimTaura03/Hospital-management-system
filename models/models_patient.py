# models/models_patient.py
from models import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))   # fixed: was 'Phone' (capital P) — caused a bug
    address = db.Column(db.String(200))