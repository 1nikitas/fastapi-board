from db.base_class import Base
from sqlalchemy import Column, Boolean, TIMESTAMP
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Float

class Lesson(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    client_id = Column(Integer)
    subject = Column(Text)
    hour_price = Column(Integer)
    duration = Column(Float)
    date = Column(TIMESTAMP)
    time = Column(Text)
    status = Column(Text, default='in process')