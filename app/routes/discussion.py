from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.discussion import DiscussionCreate, DiscussionUpdate, DiscussionResponse
from app.database import SessionLocal
from app.services.discussion_service import (
    create_discussion,
    update_discussion,
    delete_discussion,
    get_discussions_by_tags,
    get_discussions_by_text,
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/discussions/", response_model=DiscussionResponse)
def create_new_discussion(discussion: DiscussionCreate, db: Session = Depends(get_db)):
    return create_discussion(db=db, discussion=discussion)

@router.put("/discussions/{discussion_id}", response_model=DiscussionResponse)
def update_existing_discussion(discussion_id: int, discussion: DiscussionUpdate, db: Session = Depends(get_db)):
    return update_discussion(db=db, discussion_id=discussion_id, discussion=discussion)

@router.delete("/discussions/{discussion_id}")
def delete_existing_discussion(discussion_id: int, db: Session = Depends(get_db)):
    delete_discussion(db=db, discussion_id=discussion_id)
    return {"message": "Discussion deleted successfully"}

@router.get("/discussions/", response_model=list[DiscussionResponse])
def read_discussions_by_tags(tags: str, db: Session = Depends(get_db)):
    discussions = get_discussions_by_tags(db=db, tags=tags)
    return discussions

@router.get("/discussions/search/", response_model=list[DiscussionResponse])
def search_discussions(text: str, db: Session = Depends(get_db)):
    discussions = get_discussions_by_text(db=db, text=text)
    return discussions
