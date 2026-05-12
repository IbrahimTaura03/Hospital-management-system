from flask import Flask, render_template, request, redirect, url_for
from models import db


from models.models_bed import Bed
from models.models_attendance import Attendance
from models.models_task import Task
from models.models_billing import Billing

from services.services_patient import  get_all_patients
from services.services_employee import add_employee_service, get_all_employees, get_employee_by_id, update_employee_service
from services.services_medicine import add_medicine_service, get_all_medicines, get_medicine_by_id, update_medicine_service, delete_medicine_service
from services.services_bed import add_bed_service, get_all_beds, get_bed_by_id, update_bed_service, delete_bed_service
from services.services_attendance import add_attendance_service, get_all_attendance, get_attendance_by_id, update_attendance_service, delete_attendance_service
from services.services_task import add_task_service, get_all_tasks, get_task_by_id, update_task_service, delete_task_service
from services.services_billing import add_billing_service, get_all_billings, get_billing_by_id, update_billing_service, delete_billing_service

from routes.routes_patient import patient_bp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(patient_bp)

# ─── HOME ──────────────────────────────────────────────
@app.route('/')
def base():
    return render_template("base.html")





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

# ─── ATTENDANCE ────────────────────────────────────────
@app.route('/add_attendance', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        add_attendance_service(request.form)
        return redirect(url_for('view_update_attendance'))
    employees = get_all_employees()
    return render_template("add_attendance.html", employees=employees)

@app.route('/view_update_attendance')
def view_update_attendance():
    records = get_all_attendance()
    employees = get_all_employees()
    return render_template('view_update_attendance.html', records=records, employees=employees)

@app.route('/edit_attendance/<int:id>', methods=['GET', 'POST'])
def edit_attendance(id):
    record = get_attendance_by_id(id)
    if request.method == 'POST':
        update_attendance_service(id, request.form)
        return redirect(url_for('view_update_attendance'))
    employees = get_all_employees()
    return render_template('edit_attendance.html', record=record, employees=employees)

@app.route('/delete_attendance/<int:id>')
def delete_attendance(id):
    delete_attendance_service(id)
    return redirect(url_for('view_update_attendance'))

# ─── TASK ──────────────────────────────────────────────
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        add_task_service(request.form)
        return redirect(url_for('view_update_task'))
    employees = get_all_employees()
    return render_template("add_task.html", employees=employees)

@app.route('/view_update_task')
def view_update_task():
    tasks = get_all_tasks()
    employees = get_all_employees()
    return render_template('view_update_task.html', tasks=tasks, employees=employees)

@app.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = get_task_by_id(id)
    if request.method == 'POST':
        update_task_service(id, request.form)
        return redirect(url_for('view_update_task'))
    employees = get_all_employees()
    return render_template('edit_task.html', task=task, employees=employees)

@app.route('/delete_task/<int:id>')
def delete_task(id):
    delete_task_service(id)
    return redirect(url_for('view_update_task'))

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