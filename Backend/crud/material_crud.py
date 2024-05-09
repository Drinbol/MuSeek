from sqlalchemy.orm import Session
from schemas.material import MaterialCreate, MaterialUpdate
from models.models import Material, Tag


def get_material(db: Session, material_id: int):
    return db.query(Material).filter(Material.id == material_id).first()


def get_materials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Material).offset(skip).limit(limit).all()


def create_material(db: Session, material: MaterialCreate):
    db_material = Material(content=material.content)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)

    for tag_id in material.tag_ids:
        db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
        if db_tag:
            db_material.tags.append(db_tag)

    db.commit()
    return db_material


def update_material(db: Session, material_id: int, material: MaterialUpdate):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if db_material:
        db_material.content = material.content
        db_material.tags = []
        for tag_id in material.tag_ids:
            db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
            if db_tag:
                db_material.tags.append(db_tag)
        db.commit()
    return db_material


def delete_material(db: Session, material_id: int):
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
