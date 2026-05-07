from models import db
from models.models_bed import Bed

def add_bed_service(data):
    bed = Bed(
        bed_number=data['bed_number'], ward=data['ward'],
        status=data['status'],
        patient_id=data['patient_id'] if data['patient_id'] else None
    )
    db.session.add(bed)
    db.session.commit()

def get_all_beds():
    return Bed.query.all()

def get_bed_by_id(id):
    return Bed.query.get(id)

def update_bed_service(id, data):
    bed = Bed.query.get(id)
    bed.bed_number = data['bed_number'];  bed.ward = data['ward']
    bed.status = data['status']
    bed.patient_id = data['patient_id'] if data['patient_id'] else None
    db.session.commit()

def delete_bed_service(id):
    bed = Bed.query.get(id)
    db.session.delete(bed)
    db.session.commit()