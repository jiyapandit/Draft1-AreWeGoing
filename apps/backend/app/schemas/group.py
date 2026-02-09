from pydantic import BaseModel, Field
from uuid import UUID

class GroupCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    days: int = Field(ge=1, le=60)

class GroupOut(BaseModel):
    id: UUID
    name: str
    days: int

    class Config:
        from_attributes = True
