from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.discussion import DiscussionCreate, DiscussionUpdate, DiscussionResponse
from app.database import SessionLocal
from app.services.discussionService import (
    create_discussion,
    update_discussion,
    delete_discussion,
    get_discussions_by_tags,
    get_discussions_by_text,
    get_all_discussions
)
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Log to standard output (console)
    ]
)

logger = logging.getLogger(__name__)  # Create a logger instance for your module

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/createpost/", response_model=DiscussionResponse)
def create_new_discussion(discussion: DiscussionCreate, db: Session = Depends(get_db)):
    logger.info( discussion)
    return create_discussion(db=db, discussion=discussion)

@router.put("/updatepost/{discussion_id}", response_model=DiscussionResponse)
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

@router.get("/getposts", response_model=list[DiscussionResponse])
def read_discussions_by_tags(db: Session = Depends(get_db)):
    logger.info("Root endpoint accessed")
    discussions = get_all_discussions(db=db)
    return discussions