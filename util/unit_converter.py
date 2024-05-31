"""
This module contains functions for converting time units between strings and numbers.
"""

DAYS_OF_WEEK = {"sun": 1, "mon": 2, "tue": 3, "wed": 4, "thu": 5, "fri": 6, "sat": 7}

def convert_day_of_week_name_to_number(day_of_week: str) -> int:
    """Convert a day of week name to a number."""
    match day_of_week.upper():
        case "SUN":
            return 0
        case "MON":
            return 1
        case "TUE":
            return 2
        case "WED":
            return 3
        case "THU":
            return 4
        case "FRI":
            return 5
        case "SAT":
            return 6
        case _:
            raise ValueError(f"Invalid day of week name: {day_of_week}")

def convert_day_of_week_number_to_name(day_of_week: int) -> str:
    """Convert a day of week number to a name."""
    match day_of_week:
        case 0:
            return "SUN"
        case 1:
            return "MON"
        case 2:
            return "TUE"
        case 3:
            return "WED"
        case 4:
            return "THU"
        case 5:
            return "FRI"
        case 6:
            return "SAT"
        case _:
            raise ValueError(f"Invalid day of week number: {day_of_week}")

MONTH_NAMES = {
    "jan": 1, 
    "feb": 2, 
    "mar": 3, 
    "apr": 4, 
    "may": 5, 
    "jun": 6, 
    "jul": 7, 
    "aug": 8, 
    "sep": 9, 
    "oct": 10, 
    "nov": 11, 
    "dec": 12,
}

def convert_month_name_to_number(month: str) -> int:
    """Convert a month name to a number."""
    match month.upper():
        case "JAN":
            return 1
        case "FEB":
            return 2
        case "MAR":
            return 3
        case "APR":
            return 4
        case "MAY":
            return 5
        case "JUN":
            return 6
        case "JUL":
            return 7
        case "AUG":
            return 8
        case "SEP":
            return 9
        case "OCT":
            return 10
        case "NOV":
            return 11
        case "DEC":
            return 12
        case _:
            raise ValueError(f"Invalid month name: {month}")
        
def convert_month_number_to_name(month: int) -> str:
    """Convert a month number to a name."""
    match month:
        case 1:
            return "JAN"
        case 2:
            return "FEB"
        case 3:
            return "MAR"
        case 4:
            return "APR"
        case 5:
            return "MAY"
        case 6:
            return "JUN"
        case 7:
            return "JUL"
        case 8:
            return "AUG"
        case 9:
            return "SEP"
        case 10:
            return "OCT"
        case 11:
            return "NOV"
        case 12:
            return "DEC"
        case _:
            raise ValueError(f"Invalid month number: {month}")