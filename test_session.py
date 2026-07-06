from services.session import *

user = {
    "userid": 1,
    "username": "admin",
    "name": "Administrator",
    "role": "admin"
}

login(user)

print(current_user())

print(name())

print(role())

print(is_logged_in())

logout()

print(is_logged_in())