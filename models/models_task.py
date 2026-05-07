from models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    assigned_to = db.Column(db.Integer, db.ForeignKey('employee.id'))
    due_date = db.Column(db.String(20))
    status = db.Column(db.String(20), default='Pending')  # Pending / In Progress / Done