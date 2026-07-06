"""
=========================================================
GVC Math ERP
Authentication Service
Version 0.5
=========================================================
"""

from services.api import api
from services.session import (
    login as session_login,
    logout as session_logout,
    current_user
)


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass


# ---------------------------------------------------------
# Login
# ---------------------------------------------------------

def authenticate(username: str, password: str):

    username = username.strip()

    if not username:
        raise AuthenticationError("Username cannot be empty.")

    if not password:
        raise AuthenticationError("Password cannot be empty.")

    try:

        result = api.login(username, password)

    except Exception as e:

        raise AuthenticationError(str(e))

    if not result.get("success"):

        raise AuthenticationError(

            result.get(
                "message",
                "Invalid username or password."
            )

        )

    # Save user into session
    session_login(result)

    return result


# ---------------------------------------------------------
# Logout
# ---------------------------------------------------------

def logout():

    session_logout()


# ---------------------------------------------------------
# Current User
# ---------------------------------------------------------

def user():

    return current_user()


def is_authenticated():

    return current_user() is not None


def userid():

    u = current_user()

    if u:

        return u.get("userid")

    return None


def username():

    u = current_user()

    if u:

        return u.get("username")

    return ""


def name():

    u = current_user()

    if u:

        return u.get("name")

    return ""


def role():

    u = current_user()

    if u:

        return u.get("role")

    return None