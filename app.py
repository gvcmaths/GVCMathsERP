"""
=========================================================
GVC Math ERP
Main Application
Version 0.5
=========================================================
"""

from pathlib import Path

from shiny import App, ui, render, reactive
from services.auth import logout
from services.session import page, set_page
from config import (
    PAGE_LOGIN,
    PAGE_DASHBOARD
)

from services.session import page

from pages.login import (
    login_page,
    login_server
)

from pages.dashboard import dashboard
from layouts.main import main_layout

# ---------------------------------------------------------
# Static Assets
# ---------------------------------------------------------

www = Path(__file__).parent / "www"


# ---------------------------------------------------------
# User Interface
# ---------------------------------------------------------

app_ui = ui.page_fluid(

    ui.tags.head(

        ui.tags.link(
            rel="stylesheet",
            href="style.css"
        ),

        ui.tags.link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
        )

    ),

    ui.output_ui("current_page")

)


# ---------------------------------------------------------
# Server
# ---------------------------------------------------------

def server(input, output, session):

    # Initialize Login Page Logic
    login_server(input, output, session)
    from services.auth import logout
    from services.session import set_page
    from config import PAGE_LOGIN
    @reactive.effect
    @reactive.event(input.logout_btn)
    def _logout():
        logout()
        set_page(PAGE_LOGIN)

    # Reactive Page Renderer
    @output
    @render.ui
    def current_page():

        current = page()

        if current == PAGE_LOGIN:
            return login_page()

        if current == PAGE_DASHBOARD:
            return main_layout(
                dashboard()
            )
        return login_page()


# ---------------------------------------------------------
# App
# ---------------------------------------------------------

app = App(

    app_ui,

    server,

    static_assets=www

)