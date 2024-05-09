from pydantic import BaseModel
from .tag import Tag


class MaterialBase(BaseModel):
    content: str


class MaterialCreate(MaterialBase):
    tag_ids: list[int] = []


class MaterialUpdate(MaterialBase):
    tag_ids: list[int] = []


class Material(MaterialBase):
    id: int
    tags: list[Tag] = []

    class Config:
        from_attributes = True
