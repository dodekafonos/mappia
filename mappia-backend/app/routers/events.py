# app/routers/events.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

@router.get("/events/", response_model=list[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_events(db, skip, limit)

@router.post("/events/{event_id}/comments", response_model=schemas.Comment)
def add_comment(event_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, event_id, comment)

@router.get("/events/{event_id}/comments", response_model=list[schemas.Comment])
def read_comments(event_id: int, db: Session = Depends(get_db)):
    return crud.get_comments(db, event_id)
