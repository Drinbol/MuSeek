from sqlalchemy.orm import Session
from schemas.tag import TagCreate
from models.models import Tag


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tag).offset(skip).limit(limit).all()


def get_tag_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()


def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name, type=tag.type)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
