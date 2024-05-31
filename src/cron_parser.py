"""
This module contains functions that which can be used for parsing Cron Strings, and 
expands each of the fields into a list of possible values when the command will be run.
"""

import re

from .cron_response import CronResponse
from util import unit_converter

def parse_cron_string(cron_string: str) -> CronResponse:
    try:
        # parse the cron string into it's fields
        (minute, hour, day_of_month, month, day_of_week, command) = (s.lower() for s in cron_string.split(" "))
    except ValueError as e:
        raise ValueError("Invalid cron string format. Example: `*/15 0 1,15 * 1-5 \"echo 'hello world'\"`.") from e

    if "?" in minute or not validate_time_string(minute, max_unit=59):
        raise ValueError(f"Invalid minute field: {minute=}")
    
    if "?" in hour or not validate_time_string(hour, max_unit=23):
        raise ValueError(f"Invalid hour field: {hour=}")

    # TODO: validate day_of_month, day_of_week

    # Replace Month strings with their numerical values values
    for month_str, month_int in unit_converter.MONTH_NAMES.items():
        if month_str in month:
            month = month.replace(month_str, str(month_int))

    if "?" in month or not validate_time_string(month, max_unit=31, min_unit=1):
        raise ValueError(f"Invalid month field: {month=}")

    if day_of_month == "?" and day_of_week == "?":
        raise ValueError("Day of the Month and Day of the Week fields can not be `?` at the same time")
    elif "?" in day_of_month and day_of_month != "?":
        raise ValueError("Day of month field is not a valid value")
    elif "?" in day_of_week and day_of_week != "?":
        raise ValueError("Day of week field is not a valid value")

    # TODO: check for "W" and "L" in day_of_month
    if "w" in day_of_month or "l" in day_of_month:
        raise NotImplementedError("`W` and `L` are not yet supported for day_of_month")

    # Replace Day of Week strings with their numerical values values
    for day_str, day_int in unit_converter.DAYS_OF_WEEK.items():
        if day_str in day_of_week:
            day_of_week = day_of_week.replace(day_str, str(day_int))

    # TODO: check for "L" and "#" in day_of_week
    if "l" in day_of_week or "#" in day_of_week:
        raise NotImplementedError("`L` and `#` are not yet supported for day_of_week")

    # TODO: verify that minute, hour, day_of_month, month, day_of_week are nonempty
    return CronResponse(
        minute=get_time_fields(minute, min_unit=0, max_unit=59), 
        hour=get_time_fields(hour, min_unit=0, max_unit=23), 
        day_of_month=get_time_fields(day_of_month, min_unit=1, max_unit=31), 
        month=get_time_fields(month, min_unit=1, max_unit=12), 
        day_of_week=get_time_fields(day_of_week, min_unit=1, max_unit=7), 
        command=command,
    )

def get_time_fields(time_string: str, max_unit: int, min_unit: int) -> list[int]:
    if time_string == "*" or time_string == "?":
        return list(range(min_unit, max_unit + 1))  # max_unit is inclusive

    values: list[int] = []
    fields = time_string.split(",")

    for field in fields:
        if field == "*" or field == "?":
            return list(range(min_unit, max_unit + 1))
        elif field.isdigit():
            values.append(int(field))
        elif "-" in field:
            extend_using_range(values, time_string, field, max_unit, min_unit)
        elif "/" in field:
            extend_using_interval(values, time_string, field, max_unit, min_unit)
        else:
            raise ValueError(f"Unexpected format of field in time string: {field=} {time_string=}")

    if len(values) == 0:
        raise ValueError(f"Invalid time string: {time_string}")
    return values

def extend_using_range(values: list[int], time_string: str, field: str, max_unit: int, min_unit: int) -> None:
    try:
        start, end = (int(n) for n in field.split("-") if n != "") 
        values.extend(get_specified_range(min_unit, max_unit, start, end))
    except ValueError as e:
        if  e.args[0] == "too many values to unpack":
            raise ValueError(f"Unexpected field in time string: {field=} {time_string=}") from e
        elif e.args[0] == "invalid literal for int() with base 10":
            raise ValueError(f"Incorrect format for field: {field=} {time_string=}") from e
        raise ValueError(f"Invalid time string ({e}): {field=} {min_unit=} {max_unit=} {time_string=}") from e

def extend_using_interval(values: list[int], time_string: str, field: str, max_unit: int, min_unit: int) -> None:
    try:
        lst = [s for s in field.split("/") if s != ""]
        if len(lst) != 2:
            raise ValueError("Format of time string is incorrectt")

        start, interval = int(lst[0] if lst[0] != "*" else int(min_unit)), int(lst[1])
        values.extend(get_specified_range(min_unit, max_unit, start, max_unit, interval))
    except ValueError as e:
        if  e.args[0] == "too many values to unpack":
            raise ValueError(f"Unexpected field in time string: {field=} {time_string=}") from e
        elif e.args[0] == "invalid literal for int() with base 10":
            raise ValueError(f"Incorrect format for field: {field=} {time_string=}") from e
        raise ValueError(f"Invalid time string ({e}): {field=} {min_unit=} {max_unit=} {time_string=}") from e

def get_specified_range(
    min_unit: int, 
    max_unit: int, 
    start: int, 
    end: int, 
    interval: int = 1,
) -> range:
        # TODO:
        # 1. handel cases seperately
        # 2. use more discriptive error messages
        if start < min_unit or end < start or max_unit < end or interval < 1:
            raise ValueError("Interval out of bounds")

        return range(start, end + 1, interval)

def validate_time_string(time_string: str, max_unit: int, min_unit: int = 0) -> bool:
    # allow special character strings
    if time_string == "*" or time_string == "?":
        return True
    
    # verify that string contatins only the following characters
    pattern = re.compile(r"^[0-9*?/\-,]+$")
    if re.search(pattern, time_string) is None:
        return False

    # ensure all numbers are within accepted range
    for n in [s for s in re.split(r"[*?/\-,]", time_string) if s != ""]:
        if not n.isdigit() or int(n) < min_unit or max_unit < int(n):
            return False
        
    return True