from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Producto(SQLModel, table=True):
    __tablename__ = "productos"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str = ""
    precio_base: float = 0.0
    disponible: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = None