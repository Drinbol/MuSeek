from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    type: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True
