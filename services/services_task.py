from models import db
from models.models_task import Task

def add_task_service(data):
    task = Task(
        title=data['title'], description=data['description'],
        assigned_to=data['assigned_to'],
        due_date=data['due_date'], status=data['status']
    )
    db.session.add(task)
    db.session.commit()

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(id):
    return Task.query.get(id)

def update_task_service(id, data):
    task = Task.query.get(id)
    task.title = data['title'];  task.description = data['description']
    task.assigned_to = data['assigned_to']
    task.due_date = data['due_date'];  task.status = data['status']
    db.session.commit()

def delete_task_service(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()