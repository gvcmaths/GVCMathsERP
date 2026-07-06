"""
=========================================================
GVC Math ERP
Configuration
Version 0.5
=========================================================
"""

# --------------------------------------------------------
# Application
# --------------------------------------------------------

APP_NAME = "GVC Math ERP"

VERSION = "0.5"

COLLEGE = "Government Victoria College"

DEPARTMENT = "Department of Mathematics"

# --------------------------------------------------------
# Google Apps Script
# --------------------------------------------------------

API_URL = "https://script.google.com/macros/s/AKfycbz76aNDreVydz7jCxQCbp83SWJwQeGym9ZfWEeo7CoPbZJcobhDal06C-aYlfEJb5KX/exec"

# --------------------------------------------------------
# Roles
# --------------------------------------------------------

ROLE_ADMIN = "admin"

ROLE_FACULTY = "faculty"

ROLE_STUDENT = "student"

# --------------------------------------------------------
# Pages
# --------------------------------------------------------

PAGE_LOGIN = "login"

PAGE_DASHBOARD = "dashboard"

PAGE_STUDENTS = "students"

PAGE_ATTENDANCE = "attendance"

PAGE_MARKS = "marks"

PAGE_TIMETABLE = "timetable"

PAGE_RESOURCES = "resources"

PAGE_NOTICES = "notices"

PAGE_REPORTS = "reports"

PAGE_SETTINGS = "settings"

# --------------------------------------------------------
# Sidebar Menu
# --------------------------------------------------------

MENU = [

    ("house-fill", PAGE_DASHBOARD, "Dashboard"),

    ("people-fill", PAGE_STUDENTS, "Students"),

    ("calendar-check-fill", PAGE_ATTENDANCE, "Attendance"),

    ("clipboard-data-fill", PAGE_MARKS, "Internal Marks"),

    ("clock-fill", PAGE_TIMETABLE, "Timetable"),

    ("book-fill", PAGE_RESOURCES, "Course Resources"),

    ("megaphone-fill", PAGE_NOTICES, "Notices"),

    ("bar-chart-fill", PAGE_REPORTS, "Reports"),

    ("gear-fill", PAGE_SETTINGS, "Settings")

]