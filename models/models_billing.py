from models import db

class Billing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    description = db.Column(db.String(200))
    amount = db.Column(db.Float)
    date = db.Column(db.String(20))
    status = db.Column(db.String(20), default='Unpaid')   # Paid / Unpaid