class CronResponse:
    def __init__(
        self, 
        minute: list[int], 
        hour: list[int], 
        day_of_month: list[int], 
        month: list[int], 
        day_of_week: list[int], 
        command: str,
    ):
        # order values and remove duplicates
        minute, hour, day_of_month, month, day_of_week = (
            sorted(list(set(field))) for field in [minute, hour, day_of_month, month, day_of_week]
        )

        # verify that all fields are nonempty and the length of each fields 
        # falls within accepted range, e.g., at most 7 days in a week.
        if not (
            0 < len(minute) <= 60 and 
            0 < len(hour) <= 24 and 
            0 < len(day_of_month) <= 31 and 
            0 < len(month) <= 12 and 
            0 < len(day_of_week) <= 7
        ):
            # TODO: raise better error for each field
            raise ValueError("All fields must be nonempty and bounded by a valid maximum length")
        
        # TODO: ensure that each value falls withing accepted range
        
        if len(command) < 1:
            raise ValueError("Command must be nonempty")

        self.minute = minute
        self.hour = hour
        self.day_of_month = day_of_month
        self.month = month
        self.day_of_week = day_of_week
        self.command = command
