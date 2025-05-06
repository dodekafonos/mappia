# app/schemas.py
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional, List

class EventBase(BaseModel):
    title: str
    description: str
    category: str
    latitude: float
    longitude: float
    start_time: datetime
    duration: timedelta

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime

class Config:
    from_attributes = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
