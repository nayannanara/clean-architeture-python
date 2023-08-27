from src.infra.db.entities.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class UsersModel(BaseModel):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[str] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Users [id={self.id}. first_name=[{self.first_name}]"
