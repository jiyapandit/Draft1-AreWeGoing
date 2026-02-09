from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.db import get_db
from app.models.group import Group
from app.schemas.group import GroupCreate, GroupOut

router = APIRouter(prefix="/groups", tags=["groups"])

@router.post("", response_model=GroupOut)
def create_group(payload: GroupCreate, db: Session = Depends(get_db)):
    group = Group(name=payload.name, days=payload.days)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

@router.get("/{group_id}", response_model=GroupOut)
def get_group(group_id: UUID, db: Session = Depends(get_db)):
    group = db.get(Group, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
