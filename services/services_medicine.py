from models import db
from models.models_medicine import Medicine

def add_medicine_service(data):
    medicine = Medicine(
        name=data.get('name'), quantity=data.get('quantity'),
        price=data.get('price'), expiry_date=data.get('expiry_date'),
        supplier=data.get('supplier')
    )
    db.session.add(medicine)
    db.session.commit()

def get_all_medicines():
    return Medicine.query.all()

def get_medicine_by_id(id):
    return Medicine.query.get(id)

def update_medicine_service(id, data):
    med = Medicine.query.get(id)
    med.name = data.get('name');  med.quantity = data.get('quantity')
    med.price = data.get('price');  med.expiry_date = data.get('expiry_date')
    med.supplier = data.get('supplier')
    db.session.commit()

def delete_medicine_service(id):
    med = Medicine.query.get(id)
    db.session.delete(med)
    db.session.commit()