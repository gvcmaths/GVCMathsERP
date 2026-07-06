"""
=========================================================
GVC Math ERP
Header
Version 0.5
=========================================================
"""

from shiny import ui

from services.auth import name


def header():

    return ui.div(

        # ---------------------------------------------
        # Left
        # ---------------------------------------------

        ui.div(

            ui.img(
                src="logo.png",
                class_="college-logo"
            ),

            ui.div(

                ui.div(
                    "Government Victoria College",
                    class_="erp-title"

                ),
                ui.div(
                    "Department of Mathematics", 
                    class_="erp-subtitle"
                ),

                ui.div(
                    "GVC Math ERP",                    
                    class_="erp-system"
                ),

                class_="title-block"

            ),

            class_="header-left"

        ),

        # ---------------------------------------------
        # Right
        # ---------------------------------------------

        ui.div(

            ui.input_text(
                "search",
                None,
                placeholder="Search..."
            ),

            ui.tags.i(
                class_="bi bi-bell-fill top-icon"
            ),

            ui.tags.i(
                class_="bi bi-envelope-fill top-icon"
            ),

            ui.div(

                ui.tags.i(
                    class_="bi bi-person-circle"
                ),

                ui.div(

                    ui.div(
                        name(),
                        class_="admin-user"
                    ),

                ui.div(
                        "Faculty",
                        class_="user-role"
                )
            ),
            class_="user-box"            
        ),

            ui.input_action_button(

                "logout_btn",

                "Logout",

                class_="btn btn-danger"

            ),

            class_="header-right"

        ),

        class_="erp-header"

    )