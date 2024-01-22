import pytest
from src.errors.exceptions import HttpUnprocessableEntityError
from src.validators.user_finder import user_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_user_finder_validator():
    request = MockRequest()
    request.args = {}

    with pytest.raises(HttpUnprocessableEntityError) as err:
        user_finder_validator(request)
