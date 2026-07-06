"""
=========================================================
GVC Math ERP
API Service
Version 0.5
=========================================================
"""

import requests

from config import API_URL


class APIError(Exception):
    """Raised when API communication fails."""
    pass


class ERPAPI:
    """
    Google Apps Script API Client
    """

    def __init__(self):

        self.url = API_URL

    # ----------------------------------------------------
    # Generic GET
    # ----------------------------------------------------

    def get(self, action, **params):

        params["action"] = action

        try:

            response = requests.get(

                self.url,

                params=params,

                timeout=15

            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            raise APIError(str(e))

    # ----------------------------------------------------
    # Authentication
    # ----------------------------------------------------

    def login(self, username, password):

        return self.get(

            "login",

            username=username,

            password=password

        )

    # ----------------------------------------------------
    # Students
    # ----------------------------------------------------

    def students(self):

        return self.get("students")

    # ----------------------------------------------------
    # Faculty
    # ----------------------------------------------------

    def faculty(self):

        return self.get("faculty")

    # ----------------------------------------------------
    # Subjects
    # ----------------------------------------------------

    def subjects(self):

        return self.get("subjects")

    # ----------------------------------------------------
    # Timetable
    # ----------------------------------------------------

    def timetable(self):

        return self.get("timetable")

    # ----------------------------------------------------
    # Attendance
    # ----------------------------------------------------

    def attendance(self):

        return self.get("attendance")

    # ----------------------------------------------------
    # Internal Marks
    # ----------------------------------------------------

    def marks(self):

        return self.get("marks")

    # ----------------------------------------------------
    # Course Resources
    # ----------------------------------------------------

    def resources(self):

        return self.get("resources")

    # ----------------------------------------------------
    # Notices
    # ----------------------------------------------------

    def notices(self):

        return self.get("notices")


# --------------------------------------------------------
# Global API object
# --------------------------------------------------------

api = ERPAPI()