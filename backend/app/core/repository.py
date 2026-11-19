from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import SQLModel, Session, select

ModelType = TypeVar("ModelType", bound=SQLModel)

class BaseRepository(Generic[ModelType]):
    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def get_all(self) -> List[ModelType]:
        return list(self.session.exec(select(self.model)).all())

    def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.session.get(self.model, id)

    def create(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.flush() # Asigna ID sin commitear
        self.session.refresh(obj)
        return obj

    def update(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.flush()
        self.session.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.session.delete(obj)
        self.session.flush()