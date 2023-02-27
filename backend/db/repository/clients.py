from sqlalchemy import create_engine

from core.config import settings
from schemas.clients import CreateClient
from sqlalchemy.orm import Session, sessionmaker
from db.models.clients import Client
from datetime import datetime, date

today = datetime.today()

def get_today_day(day: date) -> str:
    day_number = datetime.weekday(day)
    if day_number == 0:
        return "Понедельник"
    elif day_number == 1:
        return "Вторник"
    elif day_number == 2:
        return "Среда"
    elif day_number == 3:
        return "Четверг"
    elif day_number == 4:
        return "Пятница"
    elif day_number == 5:
        return "Суббота"
    elif day_number == 6:
        return "Воскресенье"


today_day = get_today_day(today)


def create_client(client: CreateClient, db: Session):
    client_obj = Client(**client.dict())
    db.add(client_obj)
    db.commit()
    print('added!')
    return client_obj

def list_clients(db: Session):
    clients = db.query(Client).all()
    return clients

def delete_client_by_id(id: int, db: Session):
    existion_client = db.query(Client).filter(Client.id == id)
    if not existion_client:
        return 0
    existion_client.delete(synchronize_session=False)
    db.commit()
    return 1

def deactivate_client_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id)
    if not client.first():
        return 0
    client.update({'is_active': False})
    db.commit()
    return 1
def activate_client_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id)
    if not client.first():
        return 0
    client.update({'is_active': True})
    db.commit()
    return 1


def delete_user_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id)
    if not client:
        return 0

    client.delete(synchronize_session=False)
    db.commit()
    db.refresh(client)
    return 1


def get_today_clients(db: Session):

    today_clients = db.query(Client).filter(Client.day == today_day).all()
    return today_clients

def get_today_clients_amount(db: Session):
    """
    to_update: внести фильтрацию по подтверждениям
    """
    today = datetime.today()
    today_day = get_today_day(today)
    return db.query(Client).filter(Client.day == today_day).count()

def get_today_money_amount(db: Session):
    clients = db.query(Client).filter(Client.day == today_day).all()
    money = int(sum([client.hour_price*client.duration for client in clients]))
    return money

def get_today_lesson_time(db: Session):
    clients = db.query(Client).filter(Client.day == today_day).all()
    time = sum([client.duration for client in clients])
    return time

def get_cliet_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id).first()
    return client