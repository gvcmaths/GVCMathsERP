from services.auth import role

def dashboard_page():

    r = role()

    if r == "admin":
        from pages.dashboard.admin import dashboard
        return dashboard()

    elif r == "faculty":
        from pages.dashboard.faculty import dashboard
        return dashboard()

    elif r == "student":
        from pages.dashboard.student import dashboard
        return dashboard()

    return ui.h2("Unknown User")