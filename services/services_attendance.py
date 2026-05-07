from models import db
from models.models_attendance import Attendance

def add_attendance_service(data):
    attendance = Attendance(
        employee_id=data['employee_id'],
        date=data['date'],
        status=data['status']
    )
    db.session.add(attendance)
    db.session.commit()

def get_all_attendance():
    return Attendance.query.all()

def get_attendance_by_id(id):
    return Attendance.query.get(id)

def update_attendance_service(id, data):
    att = Attendance.query.get(id)
    att.employee_id = data['employee_id']
    att.date = data['date'];  att.status = data['status']
    db.session.commit()

def delete_attendance_service(id):
    att = Attendance.query.get(id)
    db.session.delete(att)
    db.session.commit()