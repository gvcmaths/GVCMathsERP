"""
=========================================================
GVC Math ERP
Timetable Service
=========================================================
"""

from services.api import api


def timetable_exists(academic_year, term):
    """
    Returns True if a timetable exists.
    """
    result = api.timetable(
        academic_year=academic_year,
        term=term
    )

    return len(result) > 0


def load_timetable(academic_year, term):
    """
    Load timetable from Google Sheets.
    """
    return api.timetable(
        academic_year=academic_year,
        term=term
    )


def create_blank_timetable(academic_year, term):
    """
    Temporary.
    Later this will generate an empty timetable.
    """
    return []


def save_timetable(data):
    """
    Temporary.
    """
    pass