from shiny import ui

from components.header import header
from components.sidebar import sidebar


def main_layout(content):

    return ui.div(

        header(),

        ui.div(

            sidebar(),

            ui.div(

                content,

                class_="main-content"

            ),

            class_="main-wrapper"

        )

    )