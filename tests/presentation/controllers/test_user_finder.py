from src.presentation.http_types.http_response import HttpResponse


def test_handle(users_finder_controller, http_request_fake):
    response = users_finder_controller.handle(http_request=http_request_fake)

    assert isinstance(response, HttpResponse)
    assert response.body == {
        "data": {
            "type": "Users",
            "count": 1,
            "attributes": {"first_name": "Nay", "last_name": "something"},
        }
    }
    assert response.status_code == 200
