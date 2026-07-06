"""
=========================================================
GVC Math ERP
Sidebar
Version 0.5
=========================================================
"""

from shiny import ui

from config import MENU


def menu_item(icon, title):

    return ui.div(

        ui.tags.i(
            class_=f"bi bi-{icon}"
        ),

        ui.span(title),

        class_="sidebar-item"

    )


def sidebar():

    items = []

    for icon, page, title in MENU:

        items.append(

            menu_item(icon, title)

        )

    return ui.div(

        ui.div(

            "MAIN MENU",

            class_="sidebar-heading"

        ),

        *items,

        ui.div(

            "Version 0.5",

            class_="sidebar-version"

        ),

        class_="sidebar"

    )