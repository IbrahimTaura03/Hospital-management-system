from flask import Blueprint, render_template, request, redirect, url_for
from models.models_billing import Billing
from services.services_billing import add_billing_service, get_all_billings, get_billing_by_id, update_billing_service, delete_billing_service
from services.services_patient import  get_all_patients

billing_bp = Blueprint('billing', __name__)

# ─── BILLING ───────────────────────────────────────────
@billing_bp.route('/add_billing', methods=['GET', 'POST'])
def add_billing():
    if request.method == 'POST':
        add_billing_service(request.form)
        return redirect(url_for('view_update_billing'))
    patients = get_all_patients()
    return render_template("add_billing.html", patients=patients)

@billing_bp.route('/view_update_billing')
def view_update_billing():
    bills = get_all_billings()
    return render_template('view_update_billing.html', bills=bills)

@billing_bp.route('/edit_billing/<int:id>', methods=['GET', 'POST'])
def edit_billing(id):
    bill = get_billing_by_id(id)
    if request.method == 'POST':
        update_billing_service(id, request.form)
        return redirect(url_for('view_update_billing'))
    patients = get_all_patients()
    return render_template('edit_billing.html', bill=bill, patients=patients)

@billing_bp.route('/delete_billing/<int:id>')
def delete_billing(id):
    delete_billing_service(id)
    return redirect(url_for('view_update_billing'))

