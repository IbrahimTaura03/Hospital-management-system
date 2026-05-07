from models import db
from models.models_billing import Billing

def add_billing_service(data):
    bill = Billing(
        patient_id=data['patient_id'], description=data['description'],
        amount=data['amount'], date=data['date'], status=data['status']
    )
    db.session.add(bill)
    db.session.commit()

def get_all_billings():
    return Billing.query.all()

def get_billing_by_id(id):
    return Billing.query.get(id)

def update_billing_service(id, data):
    bill = Billing.query.get(id)
    bill.patient_id = data['patient_id'];  bill.description = data['description']
    bill.amount = data['amount'];  bill.date = data['date']
    bill.status = data['status']
    db.session.commit()

def delete_billing_service(id):
    bill = Billing.query.get(id)
    db.session.delete(bill)
    db.session.commit()