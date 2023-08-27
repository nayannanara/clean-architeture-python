import pytest
from src.infra.db.settings.connection import DatabaseConnectionHandler


@pytest.mark.skip(reason="sensive test")
def test_create_engine_database():
    db = DatabaseConnectionHandler()
    engine = db.get_engine()

    assert engine
