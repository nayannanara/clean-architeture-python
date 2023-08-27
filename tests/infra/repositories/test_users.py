import pytest
from sqlalchemy import text
from src.infra.db.repositories.users import UsersRepository
from src.infra.db.settings.connection import database_connection_handler

connection = database_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="sensive test")
def test_create_users():
    first_name = "joaozinho"
    last_name = "de onti"
    age = 25

    users_repository = UsersRepository()
    users_repository.insert_user(first_name=first_name, last_name=last_name, age=age)

    sql = f"""
        select * from users
        where first_name = '{first_name}'
        and last_name = '{last_name}'
        and age = '{age}'
    """
    response = connection.execute(text(sql))

    result = response.fetchall()[0]

    assert result.first_name == first_name
    assert result.last_name == last_name

    connection.execute(text(f"DELETE FROM users WHERE id = '{result.id}'"))
    connection.commit()


def test_select_users():
    first_name = "fernando"
    last_name = "de hoje"
    age = 27

    sql = """
        insert into users (first_name, last_name, age) values (:first_name1, :last_name1, :age1)
    """
    params = {"first_name1": first_name, "last_name1": last_name, "age1": age}

    connection.execute(text(sql), params)
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(first_name=first_name)

    assert response[0].first_name == first_name
    assert response[0].last_name == last_name
    assert response[0].age == age

    connection.execute(text(f"DELETE FROM users WHERE id = '{response[0].id}'"))
    connection.commit()
