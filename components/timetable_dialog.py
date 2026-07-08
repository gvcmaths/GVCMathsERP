from shiny import ui


def timetable_dialog():

    return ui.modal(

        ui.input_select(
            "tt_subject",
            "Subject",
            {}
        ),

        ui.input_select(
            "tt_faculty",
            "Faculty",
            {}
        ),

        ui.input_select(
            "tt_room",
            "Room",
            {}
        ),

        title="Assign Timetable",

        footer=ui.div(

            ui.input_action_button(
                "tt_save",
                "Save",
                class_="btn btn-primary"
            ),

            ui.modal_button("Cancel")

        ),

        easy_close=False

    )