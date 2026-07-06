from services.api import api_get
from services.session import login


def authenticate(username, password):

    result = api_get(
        "login",
        username=username,
        password=password
    )

    if result.get("success"):

        login(result)

    return result
user = authenticate(username, password)

if user["success"]:
    session.login(user)