from datetime import date
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    subject: Optional[str] = None
    description: Optional[str] = None
    soft_deadline: Optional[str] = None
    deadline: Optional[str] = None
    assigned_to: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Job
class TaskCreate(TaskBase):
    title: str
    subject: str
    description: str
    soft_deadline: str
    deadline: str



# this will be used to format the response to not to have id,owner_id etc
class TaskShow(TaskBase):
    title: str
    subject: str
    description: str
    soft_deadline: str
    deadline: str
    date_posted: date
    class Config:  # to convert non dict obj to json
        orm_mode = True
