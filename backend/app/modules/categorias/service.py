from typing import List
from app.modules.categorias.schemas import CategoriaCreate, CategoriaUpdate, CategoriaRead
from app.modules.categorias.models import Categoria

class CategoriaNoEncontrada(Exception): pass
class CategoriaDuplicada(Exception): pass

class CategoriaService:
    def __init__(self, uow): self.uow = uow
    def listar(self) -> List[CategoriaRead]:
        with self.uow as uow:
            return [CategoriaRead.model_validate(c) for c in uow.categorias.get_all()]
    def obtener(self, id: int) -> CategoriaRead:
        with self.uow as uow:
            c = uow.categorias.get_by_id(id)
            if not c: raise CategoriaNoEncontrada()
            return CategoriaRead.model_validate(c)
    def crear(self, data: CategoriaCreate) -> CategoriaRead:
        with self.uow as uow:
            if uow.categorias.get_by_nombre(data.nombre): raise CategoriaDuplicada()
            c = uow.categorias.create(Categoria(**data.model_dump()))
            return CategoriaRead.model_validate(c)
    def actualizar(self, id: int, data: CategoriaUpdate) -> CategoriaRead:
        with self.uow as uow:
            c = uow.categorias.get_by_id(id)
            if not c: raise CategoriaNoEncontrada()
            for k, v in data.model_dump().items(): setattr(c, k, v)
            uow.categorias.update(c)
            return CategoriaRead.model_validate(c)
    def eliminar(self, id: int) -> None:
        with self.uow as uow:
            c = uow.categorias.get_by_id(id)
            if not c: raise CategoriaNoEncontrada()
            uow.categorias.delete(c)