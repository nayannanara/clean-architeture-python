from src.presentation.interfaces.controller import ControllerInterface
from src.domain.usecases.user_finder import UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserFinderController(ControllerInterface):
    def __init__(self, usecase: UserFinderInterface) -> None:
        self.__usecase = usecase

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]

        response = self.__usecase.find(first_name)

        return HttpResponse(status_code=200, body={"data": response})
