from db.base_class import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Float
class Client(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    subject = Column(Text)
    hour_price = Column(Integer)
    duration = Column(Float)
    is_active = Column(Boolean(), default=True)
    day = Column(Text)
    description = Column(Text, default="")