from shiny import ui
from datetime import datetime
from services.session import name
def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    elif hour < 17:
        return "Good Afternoon"

    return "Good Evening"

def dashboard():
    
    return ui.div(

        ui.h2(
            f"{greeting()}, {name()}",
            class_="page-title"
        ),

        ui.hr(),

        ui.div(

            card("📅", "Department Timetable", "goto_timetable"),
            card("👨‍🏫", "Faculty", "goto_faculty"),
            card("🎓", "Students", "goto_students"),
            card("📚", "Subjects", "goto_subjects"),
            card("📝", "Attendance", "goto_attendance"),
            card("📊", "Internal Marks", "goto_marks"),
            card("📢", "Notices", "goto_notices"),
            card("⚙️", "Settings", "goto_settings"),

            class_="dashboard-grid"

        )

    )


def card(icon, title, button_id):

    return ui.input_action_button(

        button_id,

        ui.div(

            ui.div(icon, class_="card-icon"),

            ui.div(title, class_="card-title"),

        ),

        class_="dashboard-card"

    )