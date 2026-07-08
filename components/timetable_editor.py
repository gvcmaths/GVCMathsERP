from shiny import ui


def timetable_editor():

    return ui.div(

        ui.h4("Assignment"),

        ui.hr(),

        ui.p(
            "Selected Cell",
            class_="editor-title"
        ),

        ui.output_text("selected_cell"),

        ui.br(),

        ui.input_select(
            "subject",
            "Subject",
            {}
        ),

        ui.br(),

        ui.input_select(
            "faculty",
            "Faculty",
            {}
        ),

        ui.br(),

        ui.input_select(
            "room",
            "Room",
            {}
        ),

        ui.br(),

        ui.input_action_button(
            "save_entry",
            "Save Entry",
            class_="btn btn-success w-100"
        ),

        ui.br(),

        ui.input_action_button(
            "clear_entry",
            "Clear",
            class_="btn btn-secondary w-100"
        ),

        class_="editor-panel"

    )