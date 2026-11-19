from typing import Optional
from sqlmodel import Session
from app.core.database import engine

class BaseUnitOfWork:
    session: Optional[Session] = None
    def __enter__(self):
        self.session = Session(engine)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None: self.session.commit()
            else: self.session.rollback()
        finally: self.session.close()
        return False