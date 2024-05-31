#!/usr/bin/env python3.12

"""
This file is the command-line interface for the cron-expression-parser.
"""

import argparse

from .cron_parser import parse_cron_string
from .cron_response import CronResponse

format_string = "{:<14} {:<}"
def print_time_row(name: str, values: list[int]) -> None:
    res = " ".join(str(value) for value in values)
    print(format_string.format(name, res))

def print_cron_response(cron_response: CronResponse) -> None:
    """
    Print the cron response in a human readable format.

    Args:
        cron_response (CronResponse): The cron response to print.
    """
    print_time_row("Minute", cron_response.minute)
    print_time_row("Hour", cron_response.hour)
    print_time_row("Day of Month", cron_response.day_of_month)
    print_time_row("Month", cron_response.month)
    print_time_row("Day of Week", cron_response.day_of_week)
    print(format_string.format("Command", cron_response.command))

def main() -> None:
    """
    Parse a cron string and display the times (for each field) 
    at which the command will be executed.

    Args:
        cron_string (str): A cron string in the format
        ```
        minute hour day_of_month month day_of_week command
        ```

    Raises:
        ValueError: If the cron string is not in the correct format.
    """
    parser = argparse.ArgumentParser(
        description="Parse a cron expression and display the execution times.",
    )

    parser.add_argument(
        "cron_string", 
        type=str, 
        help="A cron string in the format 'minute hour day_of_month month day_of_week command'",
    )

    args = parser.parse_args()
    cron_string = args.cron_string
    cron_response = parse_cron_string(cron_string)
    print_cron_response(cron_response)

if __name__ == "__main__":
    main()