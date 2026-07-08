from services.auth import role


def dashboard():
    print("Dispatcher called")
    r = role()
    print("Role =", r)

    if r == "Administrator":
        print("Loading Admin Dashboard")
        from pages.dashboard.admin import dashboard
        return dashboard()

    elif r == "faculty":
        from pages.dashboard.faculty import dashboard
        return dashboard()

    elif r == "student":
        from pages.dashboard.student import dashboard
        return dashboard()