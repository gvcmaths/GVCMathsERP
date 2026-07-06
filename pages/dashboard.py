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

def stat_card(icon, title, value, footer):

    return ui.div(

        ui.tags.i(class_=f"bi bi-{icon} card-icon"),

        ui.div(title, class_="card-title"),

        ui.div(str(value), class_="card-value"),

        ui.div(footer, class_="card-footer"),

        class_="dashboard-card"

    )


def panel(title, icon, *content):

    return ui.div(

        ui.div(

            ui.tags.i(class_=f"bi bi-{icon}"),

            ui.span(title),

            class_="panel-title"

        ),

        *content,

        class_="panel"

    )


def dashboard():

    return ui.div(

        # -------------------------------------------------
        # Welcome
        # -------------------------------------------------

        ui.div(

            ui.div(
                f"{greeting()}, {name()}",
                class_="welcome-title"
            ),

            ui.div(
                "Department of Mathematics • Government Victoria College",
                class_="welcome-subtitle"
            ),

            class_="welcome-box fade-in"

        ),

        # -------------------------------------------------
        # Statistics
        # -------------------------------------------------

        ui.div(

            stat_card(
                "people-fill",
                "Students",
                628,
                "View Details"
            ),

            stat_card(
                "person-workspace",
                "Faculty",
                31,
                "Faculty List"
            ),

            stat_card(
                "calendar-check",
                "Attendance",
                "96%",
                "Today's Status"
            ),

            stat_card(
                "book-fill",
                "Courses",
                42,
                "Course List"
            ),

            class_="card-grid"

        ),

        # -------------------------------------------------
        # Main Content
        # -------------------------------------------------

        ui.div(

            # ================= LEFT =====================

            ui.div(

                panel(

                    "Today's Classes",

                    "calendar-event",

                    ui.div(

                        ui.div(

                            ui.span(
                                "MSc Mathematics",
                                class_="class-name"
                            ),

                            ui.span(
                                "09:30 AM",
                                class_="class-time"
                            ),

                            class_="class-item"

                        ),

                        ui.div(

                            ui.span(
                                "BSc Semester VI",
                                class_="class-name"
                            ),

                            ui.span(
                                "11:30 AM",
                                class_="class-time"
                            ),

                            class_="class-item"

                        ),

                        ui.div(

                            ui.span(
                                "BSc Semester II",
                                class_="class-name"
                            ),

                            ui.span(
                                "02:00 PM",
                                class_="class-time"
                            ),

                            class_="class-item"

                        )

                    )

                ),

                panel(

                    "Quick Actions",

                    "lightning-fill",

                    ui.div(

                        ui.div(
                            "Take Attendance",
                            class_="action-btn"
                        ),

                        ui.div(
                            "Enter Marks",
                            class_="action-btn"
                        ),

                        ui.div(
                            "View Students",
                            class_="action-btn"
                        ),

                        ui.div(
                            "Generate Report",
                            class_="action-btn"
                        ),

                        class_="quick-actions"

                    )

                ),

                class_="left-column"

            ),

            # ================= RIGHT ====================

            ui.div(

                panel(

                    "Recent Notices",

                    "megaphone-fill",

                    ui.div(

                        ui.div(

                            ui.div(
                                "Faculty Meeting",
                                class_="notice-title"
                            ),

                            ui.div(
                                "Tomorrow 10:00 AM",
                                class_="notice-date"
                            ),

                            class_="notice-item"

                        ),

                        ui.div(

                            ui.div(
                                "Internal Marks Submission",
                                class_="notice-title"
                            ),

                            ui.div(
                                "Due: 15 July",
                                class_="notice-date"
                            ),

                            class_="notice-item"

                        ),

                        ui.div(

                            ui.div(
                                "Semester Examination",
                                class_="notice-title"
                            ),

                            ui.div(
                                "Starts next Monday",
                                class_="notice-date"
                            ),

                            class_="notice-item"

                        )

                    )

                ),

                panel(

                    "System Status",

                    "activity",

                    ui.div(

                        ui.p("✅ Google Sheets : Connected"),

                        ui.p("✅ Server : Online"),

                        ui.p("✅ Backup : Successful"),

                        ui.p("🟢 All systems operational")

                    )

                ),

                class_="right-column"

            ),

            class_="content-grid"

        ),

        ui.div(

            "GVC Math ERP  •  Version 0.5.0  •  Department of Mathematics",

            class_="footer"

        ),

        class_="dashboard"

    )