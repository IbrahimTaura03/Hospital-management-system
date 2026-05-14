from flask import Blueprint, render_template, request, redirect, url_for
from services.services_task import add_task_service, get_all_tasks, get_task_by_id, update_task_service, delete_task_service
from services.services_employee import get_all_employees
from models.models_task import Task


task_bp = Blueprint('task', __name__)

# ─── TASK ──────────────────────────────────────────────
@task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        add_task_service(request.form)
        return redirect(url_for('task.view_update_task'))
    employees = get_all_employees()
    return render_template("add_task.html", employees=employees)


@task_bp.route('/view_update_task')
def view_update_task():
    tasks = get_all_tasks()
    employees = get_all_employees()
    return render_template('view_update_task.html', tasks=tasks, employees=employees)


@task_bp.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = get_task_by_id(id)
    if request.method == 'POST':
        update_task_service(id, request.form)
        return redirect(url_for('task.view_update_task'))
    employees = get_all_employees()
    return render_template('edit_task.html', task=task, employees=employees)


@task_bp.route('/delete_task/<int:id>')
def delete_task(id):
    delete_task_service(id)
    return redirect(url_for('task.view_update_task'))
