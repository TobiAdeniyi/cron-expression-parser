import unittest

from src.cron_response import CronResponse


class TestCronResponse(unittest.TestCase):

    def test_valid_cron_response(self):
        response = CronResponse(
            minute=[0, 15, 30, 45],
            hour=[0, 12],
            day_of_month=[1, 15],
            month=[1, 6, 12],
            day_of_week=[0, 1, 2, 3, 4, 5, 6],
            command="/usr/bin/find"
        )
        self.assertEqual(response.minute, [0, 15, 30, 45])
        self.assertEqual(response.hour, [0, 12])
        self.assertEqual(response.day_of_month, [1, 15])
        self.assertEqual(response.month, [1, 6, 12])
        self.assertEqual(response.day_of_week, [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(response.command, "/usr/bin/find")

    def test_empty_field_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            CronResponse(
                minute=[],
                hour=[0, 12],
                day_of_month=[1, 15],
                month=[1, 6, 12],
                day_of_week=[0, 1, 2, 3, 4, 5, 6],
                command="/usr/bin/find"
            )
        self.assertIn("All fields must be nonempty", str(context.exception))

    def test_field_exceeds_maximum_length_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            CronResponse(
                minute=list(range(61)),
                hour=[0, 12],
                day_of_month=[1, 15],
                month=[1, 6, 12],
                day_of_week=[0, 1, 2, 3, 4, 5, 6],
                command="/usr/bin/find"
            )
        self.assertIn("All fields must be nonempty and bounded by a valid maximum length", str(context.exception))

    def test_invalid_command(self):
        with self.assertRaises(ValueError) as context:
            CronResponse(
                minute=[0, 15, 30, 45],
                hour=[0, 12],
                day_of_month=[1, 15],
                month=[1, 6, 12],
                day_of_week=[0, 1, 2, 3, 4, 5, 6],
                command=""
            )
        self.assertIn("Command must be nonempty", str(context.exception))

    # TODO: add test cases to check that all fields fall withing valid ranges, e.g., for m in minutes: assert 0 <= m <= 59

if __name__ == '__main__':
    unittest.main()