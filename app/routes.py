from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime, timezone

from . import schemas, models
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/v1/chat", response_model=schemas.PromptResponse)
def create_chat(prompt: schemas.PromptRequest, db: Session = Depends(get_db)):
    chat = models.Chat(
        id=uuid4(),
        userId=prompt.userId,
        prompt=prompt.prompt,
        response="This is a dummy response.",
        model="gpt-4",
        timestamp=datetime.now(timezone.utc)
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat
