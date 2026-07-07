from shiny import ui


def dashboard():

    return ui.div(

        ui.h2(
            "Administrator Dashboard",
            class_="page-title"
        ),

        ui.hr(),

        ui.div(

            card("📅", "Department Timetable"),
            card("👨‍🏫", "Faculty"),
            card("🎓", "Students"),
            card("📚", "Subjects"),
            card("📝", "Attendance"),
            card("📊", "Internal Marks"),
            card("📢", "Notices"),
            card("⚙️", "Settings"),

            class_="dashboard-grid"

        )

    )


def card(icon, title):

    return ui.div(

        ui.div(icon, class_="card-icon"),

        ui.div(title, class_="card-title"),

        class_="dashboard-card"

    )