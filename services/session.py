"""
=========================================================
GVC Math ERP
Application Session
Version 0.5
=========================================================
"""

from shiny import reactive

from config import (
    PAGE_LOGIN,
    PAGE_DASHBOARD
)


# ---------------------------------------------------------
# Application State
# ---------------------------------------------------------

_app_state = reactive.Value({

    "page": PAGE_LOGIN,

    "user": None

})


# ---------------------------------------------------------
# Entire State
# ---------------------------------------------------------

def state():

    return _app_state.get()


# ---------------------------------------------------------
# Current Page
# ---------------------------------------------------------

def page():

    return _app_state.get()["page"]


def set_page(page_name):

    s = _app_state.get().copy()

    s["page"] = page_name

    _app_state.set(s)


# ---------------------------------------------------------
# User
# ---------------------------------------------------------

def current_user():

    return _app_state.get()["user"]


def login(user):

    _app_state.set({

        "page": PAGE_DASHBOARD,

        "user": user

    })


def logout():

    _app_state.set({

        "page": PAGE_LOGIN,

        "user": None

    })


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def is_logged_in():

    return current_user() is not None


def userid():

    user = current_user()

    if user:

        return user.get("userid")

    return None


def username():

    user = current_user()

    if user:

        return user.get("username")

    return ""


def name():

    user = current_user()

    if user:

        return user.get("name")

    return ""


def role():

    user = current_user()

    if user:

        return user.get("role")

    return None