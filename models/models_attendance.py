from models import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    date = db.Column(db.String(20))
    status = db.Column(db.String(20))    # Present / Absent / Late