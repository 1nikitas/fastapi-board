from db.base_class import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Float
class Client(Base):
    name = Column(Text, primary_key=True)
    subject = Column(Text)
    hour_price = Column(Integer)
    duration = Column(Float)
    is_active = Column(Boolean(), default=True)
    day = Column(Text)
    description = Column(Text, default="")