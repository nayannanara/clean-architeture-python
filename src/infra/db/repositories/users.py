from typing import Any
from src.infra.db.entities.users import UsersModel
from src.infra.db.settings.connection import database_connection_handler


class UsersRepository:
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
    def select_user(cls: "UsersRepository", first_name: str) -> Any:
        with database_connection_handler as database:
            users = (
                database.session.query(UsersModel)
                .filter(UsersModel.first_name == first_name)
                .all()
            )
            return users
