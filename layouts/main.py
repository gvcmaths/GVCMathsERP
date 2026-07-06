from shiny import ui

from components.header import header
from components.sidebar import sidebar
from components.footer import footer

def main_layout(*content):

    return ui.div(

        header(),

        ui.div(

            sidebar(),

            ui.div(

                *content,
                footer(),

                class_="main-content"

            ),

            class_="main-wrapper"

        )

    )