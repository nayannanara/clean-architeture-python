from src.data.usecases.users_insert import UserInsert
from src.infra.db.repositories.users import UsersRepository
from src.presentation.controllers.user_insert import UserInsertController


def user_insert_composer():
    repository = UsersRepository()
    use_case = UserInsert(repository)
    controller = UserInsertController(use_case)

    return controller.handle
