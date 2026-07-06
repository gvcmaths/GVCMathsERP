from shiny import ui

def dashboard_card(title, value, icon):

    return ui.div(

        ui.div(
            ui.HTML(f'<i class="bi bi-{icon}"></i>'),
            class_="card-icon"
        ),

        ui.h5(title),

        ui.h2(value),

        class_="dashboard-card"
    )