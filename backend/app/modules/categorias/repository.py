from sqlmodel import select
from app.core.repository import BaseRepository
from app.modules.categorias.models import Categoria

class CategoriaRepository(BaseRepository[Categoria]):
    def __init__(self, session): super().__init__(session, Categoria)
    def get_by_nombre(self, nombre: str):
        return self.session.exec(select(Categoria).where(Categoria.nombre.ilike(nombre))).first()