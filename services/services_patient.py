from models import db
from models.models_patient import Patient

def add_patient_service(data):
    patient = Patient(
        name=data['name'],
        age=data['age'],
        phone=data['phone'],
        address=data['address']
    )
    db.session.add(patient)
    db.session.commit()

def get_all_patients():
    return Patient.query.all()

def get_patient_by_id(id):
    return Patient.query.get(id)

def update_patient_service(id, data):
    patient = Patient.query.get(id)
    patient.name = data['name']
    patient.age = data['age']
    patient.phone = data['phone']
    patient.address = data['address']
    db.session.commit()