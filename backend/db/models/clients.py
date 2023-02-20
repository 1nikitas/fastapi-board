from db.base_class import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Date

class Client(Base):
    name = Column(Text, primary_key=True)
    subject = Column(Text)
    hour_price = Column(Integer)
    is_active = Column(Boolean(), default=True)
    day = Column(Text)
    description = Column(Text, default="")