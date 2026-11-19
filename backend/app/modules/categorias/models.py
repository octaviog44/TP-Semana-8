from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = None