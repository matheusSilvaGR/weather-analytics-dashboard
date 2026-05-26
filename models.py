from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database import Base

class Clima(Base):

    __tablename__ = "clima"

    id = Column(Integer, primary_key=True, index=True)

    cidade = Column(String)

    temperatura = Column(Float)

    vento = Column(Float)

    data_registro = Column(DateTime, default=datetime.utcnow)