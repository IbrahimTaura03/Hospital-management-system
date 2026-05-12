from flask import Blueprint, render_template, request, redirect, url_for
from services.services_employee import add_employee_service, get_all_employees, get_employee_by_id, update_employee_service
from models.models_employee import Employee


employee_bp = Blueprint('employee', __name__)


@employee_bp.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        add_employee_service(request.form)
        return redirect(url_for('view_update_employee'))
    return render_template("add_employee.html")

@employee_bp.route('/view_update_employee')
def view_update_employee():
    employees = get_all_employees()
    return render_template('view_update_employee.html', employees=employees)

@employee_bp.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = get_employee_by_id(id)
    if request.method == 'POST':
        update_employee_service(id, request.form)
        return redirect(url_for('view_update_employee'))
    return render_template('edit_employee.html', employee=employee)
