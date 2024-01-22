import pytest
from src.errors.exceptions import HttpUnprocessableEntityError
from src.validators.user_insert import user_insert_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_user_insert_validator():
    request = MockRequest()
    request.json = {"first_name": 123, "last_name": "asda", "age": 12}

    with pytest.raises(HttpUnprocessableEntityError) as err:
        user_insert_validator(request)
