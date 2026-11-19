from sqlmodel import SQLModel, Session, create_engine
from app.core.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, echo=False)

def create_db_and_tables() -> None:
    from app.modules.categorias import models as _cat
    from app.modules.productos import models as _prod
    from app.modules.ingredientes import models as _ing
    from app.modules.pedidos import models as _ped
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session