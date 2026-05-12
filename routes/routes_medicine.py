from flask import Blueprint, render_template, request, redirect, url_for
from services.services_medicine import add_medicine_service, get_all_medicines, get_medicine_by_id, update_medicine_service, delete_medicine_service
from models.models_medicine import Medicine


medicine_bp = Blueprint('employee', __name__)


# ─── MEDICINE ──────────────────────────────────────────
@medicine_bp.route('/add_medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        add_medicine_service(request.form)
        return redirect(url_for('view_update_medicine'))
    return render_template("add_medicine.html")

@medicine_bp.route('/view_update_medicine')
def view_update_medicine():
    medicines = get_all_medicines()
    return render_template('view_update_medicine.html', medicines=medicines)

@medicine_bp.route('/edit_medicine/<int:id>', methods=['GET', 'POST'])
def edit_medicine(id):
    medicine = get_medicine_by_id(id)
    if request.method == 'POST':
        update_medicine_service(id, request.form)
        return redirect(url_for('view_update_medicine'))
    return render_template('edit_medicine.html', medicine=medicine)

@medicine_bp.route('/delete_medicine/<int:id>')
def delete_medicine(id):
    delete_medicine_service(id)
    return redirect(url_for('view_update_medicine'))