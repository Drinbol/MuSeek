from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base


class Material(Base):
    __tablename__ = "material"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    tags = relationship("Tag", secondary="material_tag", back_populates="materials")


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    type = Column(String(20), nullable=False)

    materials = relationship("Material", secondary="material_tag", back_populates="tags")


material_tag = Table(
    "material_tag",
    Base.metadata,
    Column("material_id", Integer, ForeignKey("material.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)
