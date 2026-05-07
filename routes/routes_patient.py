from flask import Blueprint, render_template, request, redirect, url_for
from services.services_patient import add_patient_service, get_all_patients, get_patient_by_id, update_patient_service
from models.models_patient import Patient


patient_bp = Blueprint('patient', __name__)

# ─── PATIENT ───────────────────────────────────────────

@patient_bp.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        add_patient_service(request.form)
        return redirect(url_for('view_update_patient'))
    return render_template("add_patient.html")

@patient_bp.route('/view_update_patient')
def view_update_patient():
    patients = get_all_patients()
    return render_template('view_update_patient.html', patients=patients)

@patient_bp.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = get_patient_by_id(id)
    if request.method == 'POST':
        update_patient_service(id, request.form)
        return redirect(url_for('view_update_patient'))
    return render_template('edit_patient.html', patient=patient)