from shiny import ui

from components.timetable_grid import timetable_grid


def timetable_page():

    return ui.div(

        ui.h2("Department Timetable"),

        ui.hr(),

        ui.div(

            ui.div(
                ui.strong("Academic Year : "),
                "2026-2027",
                class_="tt-info"
            ),

            ui.div(
                ui.strong("Term : "),
                "Even",
                class_="tt-info"
            ),

            ui.div(
                ui.strong("Day : "),
                ui.input_select(
                    "weekday",
                    "",
                    {
                        "Monday":"Monday",
                        "Tuesday":"Tuesday",
                        "Wednesday":"Wednesday",
                        "Thursday":"Thursday",
                        "Friday":"Friday",
                    }
                ),
                class_="tt-info"
            ),

            class_="tt-header"

        ),

        timetable_grid()

    )