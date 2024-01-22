from typing import Dict, List
from src.data.interfaces.repository import UsersRepositoryInterface
from src.domain.usecases.user_finder import UserFinderInterface
from src.errors.exceptions import HttpBadRequestError


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> dict:
        self.__validate_name(first_name=first_name)

        users = self.__search_user(first_name=first_name)
        response = self.__format_response(users=users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError("Nome inválido para a busca")

        if len(first_name) > 18:
            raise HttpBadRequestError("Nome muito grande para a busca")

    def __search_user(self, first_name: str) -> List:
        users = self.__users_repository.select_user(first_name=first_name)

        if users == []:
            raise HttpBadRequestError("Usuario não encontrado")

        return users

    @classmethod
    def __format_response(self, users: List) -> Dict:
        users = [
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
            }
            for user in users
        ]

        return {"type": "Users", "count": len(users), "attributes": users}
