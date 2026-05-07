from models import db
from models.models_employee import Employee

def add_employee_service(data):
    employee = Employee(
        name=data['name'], age=data['age'], phone=data['phone'],
        address=data['address'], role=data['role'],
        department=data['department'], salary=data['salary']
    )
    db.session.add(employee)
    db.session.commit()

def get_all_employees():
    return Employee.query.all()

def get_employee_by_id(id):
    return Employee.query.get(id)

def update_employee_service(id, data):
    emp = Employee.query.get(id)
    emp.name = data['name'];  emp.age = data['age']
    emp.phone = data['phone']; emp.address = data['address']
    emp.role = data['role'];  emp.department = data['department']
    emp.salary = data['salary']
    db.session.commit()
