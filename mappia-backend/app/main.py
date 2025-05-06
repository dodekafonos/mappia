# app/main.py
from fastapi import FastAPI
from .routers import events
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(events.router)
