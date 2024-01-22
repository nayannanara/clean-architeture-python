from typing import Any, List
from src.data.interfaces.repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.infra.db.models.users import UsersModel
from src.infra.db.settings.connection import database_connection_handler


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert_user(
        cls: "UsersRepository", first_name: str, last_name: str, age: int
    ) -> None:
        with database_connection_handler as database:
            try:
                user = UsersModel(first_name=first_name, last_name=last_name, age=age)

                database.session.add(user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls: "UsersRepository", first_name: str) -> List[Users]:
        with database_connection_handler as database:
            users = (
                database.session.query(UsersModel)
                .filter(UsersModel.first_name == first_name)
                .all()
            )
            return users
