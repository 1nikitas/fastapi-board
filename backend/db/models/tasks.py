from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    description = Column(String, nullable=False)
    soft_deadline = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    date_posted = Column(Date)
    status = Column(String, default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    assigned_to = Column(String)
    owner = relationship("User", back_populates="tasks")
    file_url = Column(String)