from src.presentation.interfaces.controller import ControllerInterface
from src.domain.usecases.user_insert import UserInsertInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserInsertController(ControllerInterface):
    def __init__(self, usecase: UserInsertInterface) -> None:
        self.__usecase = usecase

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]

        response = self.__usecase.insert(first_name, last_name, age)

        return HttpResponse(status_code=201, body={"data": response})
