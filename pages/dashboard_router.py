from services.auth import role


def dashboard():    
    r = role()
    
    if r == "Administrator":
        from pages.dashboard.admin import dashboard
        return dashboard()

    elif r == "faculty":
        from pages.dashboard.faculty import dashboard
        return dashboard()

    elif r == "student":
        from pages.dashboard.student import dashboard
        return dashboard()