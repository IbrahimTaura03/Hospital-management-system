from models import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    role = db.Column(db.String(50))        # Doctor, Nurse, Admin...
    department = db.Column(db.String(100))
    salary = db.Column(db.Float)