"""
=========================================================
GVC Math ERP
Router
=========================================================
"""

from services.session import current_user
from pages.login import login_page
from pages.dashboard import dashboard


def current_page():

    # This makes router reactive
    user = current_user()

    if user is None:
        return login_page()

    return dashboard()

    