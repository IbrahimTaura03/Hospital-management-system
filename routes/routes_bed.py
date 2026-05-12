from flask import Blueprint, render_template, request, redirect, url_for
from services.services_bed import add_bed_service, get_all_beds, get_bed_by_id, update_bed_service, delete_bed_service
from services.services_patient import get_all_patients
from models.models_bed import Bed

bed_bp = Blueprint('bed', __name__)

# ─── BED ───────────────────────────────────────────────
@bed_bp.route('/add_bed', methods=['GET', 'POST'])
def add_bed():
    if request.method == 'POST':
        add_bed_service(request.form)
        return redirect(url_for('view_update_bed'))
    patients = get_all_patients()
    return render_template("add_bed.html", patients=patients)

@bed_bp.route('/view_update_bed')
def view_update_bed():
    beds = get_all_beds()
    return render_template('view_update_bed.html', beds=beds)

@bed_bp.route('/edit_bed/<int:id>', methods=['GET', 'POST'])
def edit_bed(id):
    bed = get_bed_by_id(id)
    if request.method == 'POST':
        update_bed_service(id, request.form)
        return redirect(url_for('view_update_bed'))
    patients = get_all_patients()
    return render_template('edit_bed.html', bed=bed, patients=patients)

@bed_bp.route('/delete_bed/<int:id>')
def delete_bed(id):
    delete_bed_service(id)
    return redirect(url_for('view_update_bed'))