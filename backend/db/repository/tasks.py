from db.models.tasks import Task
from schemas.tasks import TaskCreate
from sqlalchemy.orm import Session


def create_new_task(task: TaskCreate, db: Session, owner_id: int):
    task = Task(**task.dict(), owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def retreive_task(id: int, db: Session):
    item = db.query(Task).filter(Task.id == id).first()
    return item


def list_tasks(db: Session):
    tasks = db.query(Task).all()
    return tasks


def update_task_by_id(id: int, task: TaskCreate, db: Session, owner_id):
    existing_task = db.query(Task).filter(Task.id == id)
    if not existing_task.first():
        return 0
    task.__dict__.update(
        owner_id=owner_id
    )  # update dictionary with new key value of owner_id
    existing_task.update(task.__dict__)
    db.commit()
    return 1


def delete_task_by_id(id: int, db: Session, owner_id):
    existing_task = db.query(Task).filter(Task.id == id)
    if not existing_task.first():
        return 0
    existing_task.delete(synchronize_session=False)
    db.commit()
    return 1


def search_task(query: str, db: Session):
    tasks = db.query(Task).filter(Task.title.contains(query))
    return tasks

def tasks_assigned_to_me(id: int, db: Session):
    tasks = db.query(Task).filter(Task.assigned_to == id).all()
    return tasks