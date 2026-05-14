from flask import Blueprint, render_template, request, redirect, url_for
from services.services_attendance import add_attendance_service, get_all_attendance, get_attendance_by_id, update_attendance_service, delete_attendance_service
from services.services_employee import get_all_employees
from models.models_attendance import Attendance


attendance_bp = Blueprint('attendance', __name__)

# ─── ATTENDANCE ────────────────────────────────────────
@attendance_bp.route('/add_attendance', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        add_attendance_service(request.form)
        return redirect(url_for('attendance.view_update_attendance'))
    employees = get_all_employees()
    return render_template("add_attendance.html", employees=employees)


@attendance_bp.route('/view_update_attendance')
def view_update_attendance():
    records = get_all_attendance()
    employees = get_all_employees()
    return render_template('view_update_attendance.html', records=records, employees=employees)


@attendance_bp.route('/edit_attendance/<int:id>', methods=['GET', 'POST'])
def edit_attendance(id):
    record = get_attendance_by_id(id)
    if request.method == 'POST':
        update_attendance_service(id, request.form)
        return redirect(url_for('attendance.view_update_attendance'))
    employees = get_all_employees()
    return render_template('edit_attendance.html', record=record, employees=employees)


@attendance_bp.route('/delete_attendance/<int:id>')
def delete_attendance(id):
    delete_attendance_service(id)
    return redirect(url_for('attendance.view_update_attendance'))
