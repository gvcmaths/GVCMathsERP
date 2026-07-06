"""
=========================================================
GVC Math ERP
Login Page
Version 0.5
=========================================================
"""

from shiny import ui, reactive, render

from services.auth import authenticate, AuthenticationError


# =========================================================
# Login UI
# =========================================================

def login_page():

    return ui.div(

        ui.div(

            ui.img(
                src="logo.png",
                class_="login-logo"
            ),

            ui.h2(
                "GVC Math ERP",
                class_="login-title"
            ),

            ui.p(
                "Department of Mathematics",
                class_="login-subtitle"
            ),

            ui.p(
                "Government Victoria College, Palakkad",
                class_="login-college"
            ),

            ui.hr(),

            ui.input_text(
                "username",
                "Username",
                placeholder="Enter Username",
                width="100%"
            ),

            ui.br(),

            ui.input_password(
                "password",
                "Password",
                placeholder="Enter Password",
                width="100%"
            ),

            ui.br(),

            ui.input_action_button(

                "login_btn",

                "🔐 Login",

                class_="btn-login"

            ),

            ui.br(),
            ui.br(),

            ui.output_ui("login_message"),

            ui.hr(),

            ui.div(

                "Version 0.5",

                class_="login-version"

            ),

            class_="login-card"

        ),

        class_="login-container"

    )


# =========================================================
# Login Server
# =========================================================

def login_server(input, output, session):

    login_error = reactive.Value("")

    @reactive.effect
    @reactive.event(input.login_btn)
    def _():

        try:

            authenticate(

                input.username(),

                input.password()

            )

            login_error.set("")

        except AuthenticationError as e:

            login_error.set(str(e))

    @output
    @render.ui
    def login_message():

        msg = login_error.get()

        if msg == "":

            return ui.div()

        return ui.div(

            msg,

            class_="alert alert-danger"

        )