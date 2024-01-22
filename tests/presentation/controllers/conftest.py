from typing import Dict
import pytest

from src.presentation.controllers.user_finder import UserFinderController


class UserFindFake:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, first_name: str) -> Dict:
        self.find_attributes["first_name"] = first_name

        return {
            "type": "Users",
            "count": 1,
            "attributes": {"first_name": first_name, "last_name": "something"},
        }


class HttpRequestFake:
    def __init__(self) -> None:
        self.query_params = {"first_name": "Nay"}


@pytest.fixture
def usecase_find_fake():
    return UserFindFake()


@pytest.fixture
def users_finder_controller(usecase_find_fake):
    return UserFinderController(usecase=usecase_find_fake)


@pytest.fixture
def http_request_fake():
    return HttpRequestFake()
