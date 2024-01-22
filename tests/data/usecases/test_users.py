import pytest


def test_find_users_return_success(users_finder_usecase):
    response = users_finder_usecase.find(first_name="Nay")

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []


def test_find_users_return_name_invalid(users_finder_usecase):
    with pytest.raises(Exception) as err:
        users_finder_usecase.find(first_name="Nay123")

    err.value.args[0] == "Nome inválido para a busca"


def test_find_users_return_name_length_invalid(users_finder_usecase):
    with pytest.raises(Exception) as err:
        users_finder_usecase.find(first_name="Naydnaskdasadasdasdasd")

    err.value.args[0] == "Nome muito grande para a busca"


def test_find_users_return_empty_list(mocker, users_finder_usecase):
    mocker.patch(
        "tests.data.usecases.conftest.UsersRepositoryFake.select_user", return_value=[]
    )

    with pytest.raises(Exception) as err:
        users_finder_usecase.find(first_name="Nay")

    err.value.args[0] == "Usuario não encontrado"


def test_insert_users_return_success(users_insert_usecase):
    response = users_insert_usecase.insert(first_name="Nay", last_name="Nara", age=26)

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"] == {
        "first_name": "Nay",
        "last_name": "Nara",
        "age": 26,
    }
