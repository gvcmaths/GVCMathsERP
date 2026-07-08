from shiny import ui


# ---------------------------------------------------------
# Timetable Columns
# ---------------------------------------------------------

def timetable_columns(term):
    """
    Returns the timetable columns.

    Each column knows:
        Programme
        Semester
        Display Label
    """

    if term == "Odd":

        return [

            {"programme": "BSc", "semester": 1, "label": "BSc I"},
            {"programme": "BSc", "semester": 3, "label": "BSc III"},
            {"programme": "BSc", "semester": 5, "label": "BSc V"},
            {"programme": "BSc", "semester": 7, "label": "BSc VII"},

            {"programme": "MSc", "semester": 1, "label": "MSc I"},
            {"programme": "MSc", "semester": 3, "label": "MSc III"}

        ]

    return [

        {"programme": "BSc", "semester": 2, "label": "BSc II"},
        {"programme": "BSc", "semester": 4, "label": "BSc IV"},
        {"programme": "BSc", "semester": 6, "label": "BSc VI"},
        {"programme": "BSc", "semester": 8, "label": "BSc VIII"},

        {"programme": "MSc", "semester": 2, "label": "MSc II"},
        {"programme": "MSc", "semester": 4, "label": "MSc IV"}

    ]


# ---------------------------------------------------------
# Timetable Grid
# ---------------------------------------------------------

def timetable_grid(columns, day="Monday"):

    header = ui.tags.tr(

        ui.tags.th("Period"),

        *[
            ui.tags.th(col["label"])
            for col in columns
        ]

    )

    rows = []

    # Forenoon

    for period in [1, 2, 3]:

        rows.append(

            timetable_row(
                day,
                period,
                columns
            )

        )

    # Lunch

    rows.append(

        ui.tags.tr(

            ui.tags.td(

                "Lunch Break",

                colspan=len(columns) + 1,

                class_="lunch-row"

            )

        )

    )

    # Afternoon

    for period in [4, 5]:

        rows.append(

            timetable_row(
                day,
                period,
                columns
            )

        )

    return ui.tags.table(

        ui.tags.thead(header),

        ui.tags.tbody(*rows),

        class_="timetable-grid"

    )


# ---------------------------------------------------------
# One Row
# ---------------------------------------------------------

def timetable_row(day, period, columns):

    cells = [

        ui.tags.td(

            f"P{period}",

            class_="period-cell"

        )

    ]

    for col in columns:

        cell_id = (

            f"{day}_"

            f"{col['programme']}_"

            f"{col['semester']}_"

            f"P{period}"

        )

        cells.append(

            ui.tags.td(

                "",

                id=cell_id,

                class_="tt-cell"

            )

        )

    return ui.tags.tr(*cells)