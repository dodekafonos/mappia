# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(
        title=event.title,
        description=event.description,
        category=event.category,
        location=from_shape(Point(event.longitude, event.latitude), srid=4326),
        start_time=event.start_time,
        duration=event.duration,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_comment(db: Session, event_id: int, comment: schemas.CommentCreate):
    db_comment = models.Comment(
        event_id=event_id,
        text=comment.text
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, event_id: int):
    return db.query(models.Comment).filter(models.Comment.event_id == event_id).all()
