# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Interval, ForeignKey
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    category = Column(String(50))
    location = Column(Geography(geometry_type='POINT', srid=4326))
    start_time = Column(DateTime)
    duration = Column(Interval)
    created_at = Column(DateTime, default=datetime.utcnow)

    comments = relationship("Comment", back_populates="event")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    event = relationship("Event", back_populates="comments")
