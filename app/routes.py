from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime, timezone

from . import schemas, models
from .database import SessionLocal
from .services.openrouter_service import get_openrouter_response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/v1/chat", response_model=schemas.PromptResponse)
def create_chat(prompt: schemas.PromptRequest, db: Session = Depends(get_db)):
    try:
        chat_response, model_used = get_openrouter_response(prompt.prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    chat = models.Chat(
        id=uuid4(),
        userId=prompt.userId,
        prompt=prompt.prompt,
        response=chat_response,
        model=model_used,
        timestamp=datetime.now(timezone.utc)
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat
