from sqlalchemy.orm import Session
from app.models.discussion import Discussion
from app.schemas.discussion import DiscussionCreate, DiscussionUpdate
from fastapi import HTTPException
from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger(__name__)
def create_discussion(db: Session, discussion: DiscussionCreate):
    db_discussion = Discussion(**discussion.dict())
    logger.info(db_discussion)
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def update_discussion(db: Session, discussion_id: int, discussion: DiscussionUpdate):
    db_discussion = db.query(Discussion).filter(Discussion.id == discussion_id).first()
    if not db_discussion:
        raise HTTPException(status_code=404, detail="Discussion not found")
    for key, value in discussion.dict().items():
        setattr(db_discussion, key, value)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def delete_discussion(db: Session, discussion_id: int):
    db_discussion = db.query(Discussion).filter(Discussion.id == discussion_id).first()
    if not db_discussion:
        raise HTTPException(status_code=404, detail="Discussion not found")
    db.delete(db_discussion)
    db.commit()

def get_discussions_by_tags(db: Session, tags: str):
    return db.query(Discussion).filter(Discussion.hashtags.ilike(f"%{tags}%")).all()

def get_discussions_by_text(db: Session, text: str):
    return db.query(Discussion).filter(Discussion.text.ilike(f"%{text}%")).all()
def get_all_discussions(db: Session):
    return db.query(Discussion).all()

# es = Elasticsearch()

# def index_discussion(discussion):
#     es.index(index="discussions", id=discussion.id, body={
#         "text": discussion.text,
#         "hashtags": discussion.hashtags,
#         "created_on": discussion.created_on,
#         "user_id": discussion.user_id
#     })

# def search_discussions_by_hashtags(tags: str):
#     response = es.search(index="discussions", body={
#         "query": {
#             "match": {
#                 "hashtags": tags
#             }
#         }
#     })
#     return response['hits']['hits']
