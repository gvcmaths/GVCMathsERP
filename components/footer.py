"""
=========================================================
GVC Math ERP
Footer
Version 0.5
=========================================================
"""

from shiny import ui
from datetime import datetime

year = datetime.now().year

def footer():

    return ui.div(

        ui.div(

            f"© {year} Department of Mathematics",

            class_="footer-title"

        ),

        ui.div(

            "Government Victoria College, Palakkad",

            class_="footer-subtitle"

        ),

        ui.div(

            "Version 0.5.0",

            class_="footer-version"

        ),

        class_="erp-footer"

    )