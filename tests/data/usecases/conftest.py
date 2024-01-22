from typing import Dict, List

import pytest
from src.data.usecases.users_finder import UserFinder
from src.data.usecases.users_insert import UserInsert
from src.domain.models.users import Users
from src.presentation.controllers.user_finder import UserFinderController


class UsersRepositoryFake:
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [Users(23, first_name, "last", 43), Users(23, first_name, "last_2", 12)]


@pytest.fixture
def users_repository_fake():
    return UsersRepositoryFake()


@pytest.fixture
def users_finder_usecase(users_repository_fake):
    return UserFinder(users_repository=users_repository_fake)


@pytest.fixture
def users_insert_usecase(users_repository_fake):
    return UserInsert(users_repository=users_repository_fake)
