from flask import Flask, render_template, request, redirect, url_for
from models import db
from models.models_employee import Employee
from models.models_medicine import Medicine
from models.models_bed import Bed
from models.models_billing import Billing

from services.services_patient import  get_all_patients
from services.services_employee import add_employee_service, get_all_employees, get_employee_by_id, update_employee_service
from services.services_medicine import add_medicine_service, get_all_medicines, get_medicine_by_id, update_medicine_service, delete_medicine_service
from services.services_bed import add_bed_service, get_all_beds, get_bed_by_id, update_bed_service, delete_bed_service
from services.services_billing import add_billing_service, get_all_billings, get_billing_by_id, update_billing_service, delete_billing_service

from routes.routes_patient import patient_bp

from routes.routes_attendance import attendance_bp
from routes.routes_task import task_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(patient_bp)

app.register_blueprint(attendance_bp)
app.register_blueprint(task_bp)

# ─── HOME ──────────────────────────────────────────────
@app.route('/')
def base():
    return render_template("base.html")



# ─── EMPLOYEE ──────────────────────────────────────────
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        add_employee_service(request.form)
        return redirect(url_for('view_update_employee'))
    return render_template("add_employee.html")

@app.route('/view_update_employee')
def view_update_employee():
    employees = get_all_employees()
    return render_template('view_update_employee.html', employees=employees)

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = get_employee_by_id(id)
    if request.method == 'POST':
        update_employee_service(id, request.form)
        return redirect(url_for('view_update_employee'))
    return render_template('edit_employee.html', employee=employee)


# ─── MEDICINE ──────────────────────────────────────────
@app.route('/add_medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        add_medicine_service(request.form)
        return redirect(url_for('view_update_medicine'))
    return render_template("add_medicine.html")

@app.route('/view_update_medicine')
def view_update_medicine():
    medicines = get_all_medicines()
    return render_template('view_update_medicine.html', medicines=medicines)

@app.route('/edit_medicine/<int:id>', methods=['GET', 'POST'])
def edit_medicine(id):
    medicine = get_medicine_by_id(id)
    if request.method == 'POST':
        update_medicine_service(id, request.form)
        return redirect(url_for('view_update_medicine'))
    return render_template('edit_medicine.html', medicine=medicine)

@app.route('/delete_medicine/<int:id>')
def delete_medicine(id):
    delete_medicine_service(id)
    return redirect(url_for('view_update_medicine'))

# ─── BED ───────────────────────────────────────────────
@app.route('/add_bed', methods=['GET', 'POST'])
def add_bed():
    if request.method == 'POST':
        add_bed_service(request.form)
        return redirect(url_for('view_update_bed'))
    patients = get_all_patients()
    return render_template("add_bed.html", patients=patients)

@app.route('/view_update_bed')
def view_update_bed():
    beds = get_all_beds()
    return render_template('view_update_bed.html', beds=beds)

@app.route('/edit_bed/<int:id>', methods=['GET', 'POST'])
def edit_bed(id):
    bed = get_bed_by_id(id)
    if request.method == 'POST':
        update_bed_service(id, request.form)
        return redirect(url_for('view_update_bed'))
    patients = get_all_patients()
    return render_template('edit_bed.html', bed=bed, patients=patients)

@app.route('/delete_bed/<int:id>')
def delete_bed(id):
    delete_bed_service(id)
    return redirect(url_for('view_update_bed'))



# ─── BILLING ───────────────────────────────────────────
@app.route('/add_billing', methods=['GET', 'POST'])
def add_billing():
    if request.method == 'POST':
        add_billing_service(request.form)
        return redirect(url_for('view_update_billing'))
    patients = get_all_patients()
    return render_template("add_billing.html", patients=patients)

@app.route('/view_update_billing')
def view_update_billing():
    bills = get_all_billings()
    return render_template('view_update_billing.html', bills=bills)

@app.route('/edit_billing/<int:id>', methods=['GET', 'POST'])
def edit_billing(id):
    bill = get_billing_by_id(id)
    if request.method == 'POST':
        update_billing_service(id, request.form)
        return redirect(url_for('view_update_billing'))
    patients = get_all_patients()
    return render_template('edit_billing.html', bill=bill, patients=patients)

@app.route('/delete_billing/<int:id>')
def delete_billing(id):
    delete_billing_service(id)
    return redirect(url_for('view_update_billing'))

if __name__ == '__main__':
    app.run(debug=True)