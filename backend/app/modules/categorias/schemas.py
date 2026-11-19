from typing import Annotated
from pydantic import StringConstraints
from sqlmodel import SQLModel

NombreStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class CategoriaBase(SQLModel):
    nombre: NombreStr
    descripcion: str = ""

class CategoriaCreate(CategoriaBase): ...
class CategoriaUpdate(CategoriaBase): ...
class CategoriaRead(CategoriaBase):
    id: int