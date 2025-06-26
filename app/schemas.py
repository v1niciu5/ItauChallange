from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PromptRequest(BaseModel):
    userId: str
    prompt: str

class PromptResponse(BaseModel):
    id: UUID
    userId: str
    prompt: str
    response: str
    model: str
    timestamp: datetime
