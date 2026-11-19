from typing import Annotated
from pydantic import Field, StringConstraints
from sqlmodel import SQLModel

NombreStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class ProductoBase(SQLModel):
    nombre: NombreStr
    descripcion: str = ""
    precio_base: float = Field(ge=0)  # RN-07
    disponible: bool = True

class ProductoCreate(ProductoBase): ...
class ProductoUpdate(ProductoBase): ...
class ProductoRead(ProductoBase): id: int