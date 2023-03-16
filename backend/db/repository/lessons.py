from sqlalchemy import create_engine

from core.config import settings
from schemas.clients import CreateClient
from sqlalchemy.orm import Session, sessionmaker
from db.models.clients import Client
from datetime import datetime, date


from sqlalchemy.orm import Session

from db.models.clients import Client
from db.models.lessons import Lesson

def lesson_exists(client_id: int, db: Session):
    lessons = db.query(Lesson).filter(Lesson.id == client_id).first()

    if not lessons:
        return False
    return True

def create_lesson_today(client: Client, db: Session):
    if not lesson_exists(client.id, db=db):
        db.add(Lesson(**{'name':client.name,
                'subject': client.subject,
                'hour_price': client.hour_price,
                'client_id': client.id,
                'date': datetime.today(),
                'duration': client.duration,
                'time': client.time
                })
                )
        db.commit()



def get_today_lessons(db: Session):
    lessons = db.query(Lesson).filter()
    return lessons