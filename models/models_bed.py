from models import db

class Bed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bed_number = db.Column(db.String(20))
    ward = db.Column(db.String(100))
    status = db.Column(db.String(20), default='Available')  # Available / Occupied
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=True)