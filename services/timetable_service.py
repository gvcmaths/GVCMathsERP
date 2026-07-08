"""
=========================================================
GVC Math ERP
Timetable Service
=========================================================
"""

from services.api import api


class TimetableError(Exception):
    pass


def timetable_exists(academic_year, term):

    result = api.timetable(
        academic_year=academic_year,
        term=term
    )

    if not result["success"]:
        raise TimetableError("Unable to load timetable")

    return len(result["timetable"]) > 0


def load_timetable(academic_year, term):

    result = api.timetable(
        academic_year=academic_year,
        term=term
    )

    if not result["success"]:
        raise TimetableError("Unable to load timetable")

    return result["timetable"]


def create_blank_timetable():

    return []


def save_timetable(data):

    # We will implement this later.

    pass