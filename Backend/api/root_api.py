from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.material import Material, MaterialCreate, MaterialUpdate
from schemas.tag import Tag, TagCreate
from crud.material_crud import create_material, get_materials, get_material, update_material, delete_material
from crud.tag_crud import create_tag, get_tags, get_tag_by_name
router = APIRouter()


@router.post("/materials/", response_model=Material)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    return create_material(db=db, material=material)


@router.get("/materials/", response_model=list[Material])
def read_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    materials = get_materials(db, skip=skip, limit=limit)
    return materials


@router.get("/materials/{material_id}", response_model=Material)
def read_material(material_id: int, db: Session = Depends(get_db)):
    db_material = get_material(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@router.put("/materials/{material_id}", response_model=Material)
def update_material(material_id: int, material: MaterialUpdate, db: Session = Depends(get_db)):
    db_material = update_material(db, material_id=material_id, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@router.delete("/materials/{material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db)):
    db_material = delete_material(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return {"message": "Material deleted"}


@router.post("/tags/", response_model=Tag)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = get_tag_by_name(db, name=tag.name)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return create_tag(db=db, tag=tag)


@router.get("/tags/", response_model=list[Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = get_tags(db, skip=skip, limit=limit)
    return tags
