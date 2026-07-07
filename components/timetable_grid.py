from shiny import ui

CLASSES = [
    "BSc I",
    "BSc II",
    "BSc III",
    "MSc I",
    "MSc II",
]


def timetable_grid():

    header = ui.tags.tr(
        ui.tags.th("Period"),
        *[ui.tags.th(c) for c in CLASSES]
    )

    rows = []

    for period in [1, 2, 3]:
        rows.append(_row(period))

    rows.append(
        ui.tags.tr(
            ui.tags.td(
                "Lunch Break",
                colspan="6",
                class_="lunch-row"
            )
        )
    )

    for period in [4, 5]:
        rows.append(_row(period))

    return ui.tags.table(
        ui.tags.thead(header),
        ui.tags.tbody(*rows),
        class_="timetable-grid"
    )


def _row(period):

    return ui.tags.tr(

        ui.tags.td(f"Period {period}", class_="period-cell"),

        *[
            ui.tags.td("+", class_="tt-cell")
            for _ in CLASSES
        ]
    )