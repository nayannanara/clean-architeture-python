from typing import Dict, List
from src.data.interfaces.repository import UsersRepositoryInterface
from src.domain.usecases.user_insert import UserInsertInterface


class UserInsert(UserInsertInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def insert(self, first_name: str, last_name: str, age: int) -> dict:
        self.__validate_name(name=first_name)
        self.__validate_name(name=last_name)

        self.__insert_user(first_name=first_name, last_name=last_name, age=age)
        response = self.__format_response(
            first_name=first_name, last_name=last_name, age=age
        )

        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception("Nome inválido para a busca")

        if len(name) > 18:
            raise Exception("Nome muito grande para a busca")

    def __insert_user(self, first_name: str, last_name: str, age: int) -> List:
        self.__users_repository.insert_user(
            first_name=first_name, last_name=last_name, age=age
        )

    @classmethod
    def __format_response(self, first_name: str, last_name: str, age: int) -> Dict:
        return {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            },
        }
