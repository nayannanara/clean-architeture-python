from src.data.usecases.users_finder import UserFinder
from src.infra.db.repositories.users import UsersRepository
from src.presentation.controllers.user_finder import UserFinderController


def user_finder_composer():
    repository = UsersRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)

    return controller.handle
