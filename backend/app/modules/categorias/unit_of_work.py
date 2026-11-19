from sqlmodel import Session
from app.core.database import engine
from app.modules.categorias.repository import CategoriaRepository
from app.modules.productos.repository import ProductoRepository

class CategoriaUnitOfWork:
    def __enter__(self):
        self.session = Session(engine)
        self.categorias = CategoriaRepository(self.session)
        self.productos = ProductoRepository(self.session)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None: self.session.commit()
            else: self.session.rollback()
        finally: self.session.close()
        return False