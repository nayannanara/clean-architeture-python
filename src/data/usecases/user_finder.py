from src.domain.usecases.user_finder import UserFinderInterface
from src.infra.db.repositories.users import UsersRepository


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepository) -> None:
        self.users_repository = users_repository

    def find(self, first_name: str) -> dict:
        return super().find(first_name)
