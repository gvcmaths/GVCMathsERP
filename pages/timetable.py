"""
=========================================================
GVC Math ERP
Department Timetable
=========================================================
"""

from shiny import ui, render, reactive

from components.timetable_grid import (
    timetable_grid,
    timetable_columns
)

from components.timetable_editor import (
    timetable_editor
)


# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

def timetable_page():

    return ui.div(

        ui.h2(
            "Department Timetable",
            class_="page-title"
        ),

        ui.hr(),

        # -------------------------------------------------
        # Toolbar
        # -------------------------------------------------

        ui.div(

            ui.div(

                ui.input_select(
                    "academic_year",
                    "Academic Year",
                    {
                        "2025-2026": "2025-2026",
                        "2026-2027": "2026-2027",
                        "2027-2028": "2027-2028",
                    },
                ),

                class_="toolbar-item"

            ),

            ui.div(

                ui.input_select(
                    "term",
                    "Term",
                    {
                        "Odd": "Odd",
                        "Even": "Even"
                    },
                ),

                class_="toolbar-item"

            ),

            ui.div(

                ui.br(),

                ui.input_action_button(
                    "open_tt",
                    "Open",
                    class_="btn btn-primary"
                ),

                class_="toolbar-item"

            ),

            ui.div(

                ui.br(),

                ui.input_action_button(
                    "save_tt",
                    "Save Timetable",
                    class_="btn btn-success"
                ),

                class_="toolbar-item"

            ),

            class_="tt-toolbar"

        ),

        ui.br(),

        # -------------------------------------------------
        # Day Buttons
        # -------------------------------------------------

        ui.div(

            ui.input_action_button(
                "day_mon",
                "Monday",
                class_="day-btn active-day"
            ),

            ui.input_action_button(
                "day_tue",
                "Tuesday",
                class_="day-btn"
            ),

            ui.input_action_button(
                "day_wed",
                "Wednesday",
                class_="day-btn"
            ),

            ui.input_action_button(
                "day_thu",
                "Thursday",
                class_="day-btn"
            ),

            ui.input_action_button(
                "day_fri",
                "Friday",
                class_="day-btn"
            ),

            class_="day-bar"

        ),

        ui.br(),

        # -------------------------------------------------
        # Main Layout
        # -------------------------------------------------

        ui.row(

            ui.column(

                9,

                ui.output_ui("tt_grid")

            ),

            ui.column(

                3,

                timetable_editor()

            )

        )

    )


# ---------------------------------------------------------
# SERVER
# ---------------------------------------------------------

def timetable_server(input, output, session):

    current_day = reactive.Value("Monday")

    # -----------------------------
    # Day Buttons
    # -----------------------------

    @reactive.effect
    @reactive.event(input.day_mon)
    def _():
        current_day.set("Monday")

    @reactive.effect
    @reactive.event(input.day_tue)
    def _():
        current_day.set("Tuesday")

    @reactive.effect
    @reactive.event(input.day_wed)
    def _():
        current_day.set("Wednesday")

    @reactive.effect
    @reactive.event(input.day_thu)
    def _():
        current_day.set("Thursday")

    @reactive.effect
    @reactive.event(input.day_fri)
    def _():
        current_day.set("Friday")

    # -----------------------------
    # Timetable Grid
    # -----------------------------

    @output
    @render.ui
    def tt_grid():

        columns = timetable_columns(
            input.term()
        )

        return timetable_grid(

            columns,

            day=current_day()

        )

    # -----------------------------
    # Open
    # -----------------------------

    @reactive.effect
    @reactive.event(input.open_tt)
    def _():

        print("--------------------------------")

        print("Academic Year :", input.academic_year())

        print("Term          :", input.term())

        print("Day           :", current_day())

        print("--------------------------------")