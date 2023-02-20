from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class LoggedUser(Base):
    token = Column(String, primary_key=True)