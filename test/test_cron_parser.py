import unittest

from src.cron_response import CronResponse
from src.cron_parser import (
    validate_time_string,
    parse_cron_string,
    get_time_fields,
)


class TestParseCronString(unittest.TestCase):

    def test_valid_day_of_month_and_day_of_week(self):
        cron_string = "0 0 1,15 * 1-5 /usr/bin/find"
        response = parse_cron_string(cron_string)

        expected_response = CronResponse(
            minute=[0],
            hour=[0],
            day_of_month=[1, 15],
            month=list(range(1, 13)),
            day_of_week=list(range(1, 6)),
            command="/usr/bin/find"
        )

        self.assertEqual(response.minute, expected_response.minute)
        self.assertEqual(response.hour, expected_response.hour)
        self.assertEqual(response.day_of_month, expected_response.day_of_month)
        self.assertEqual(response.month, expected_response.month)
        self.assertEqual(response.day_of_week, expected_response.day_of_week)
        self.assertEqual(response.command, expected_response.command)

    # TODO: implement logic for this
    # def test_invalid_day_of_month_question_mark(self):
    #     cron_string = "0 0 ? * 1-35 /usr/bin/find"
    #     with self.assertRaises(ValueError) as context:
    #         parse_cron_string(cron_string)
    #     self.assertIn("Day of month field is not a valid value", str(context.exception))

    def test_invalid_minute_question_mark(self):
        cron_string = "? 0 1,15 1 * /usr/bin/find"
        with self.assertRaises(ValueError) as context:
            parse_cron_string(cron_string)
        self.assertIn("Invalid minute field: minute='?'", str(context.exception))

    def test_invalid_hour_question_mark(self):
        cron_string = "0 ? 1,15 1 * /usr/bin/find"
        with self.assertRaises(ValueError) as context:
            parse_cron_string(cron_string)
        self.assertIn("Invalid hour field: hour='?'", str(context.exception))

    def test_invalid_month_question_mark(self):
        cron_string = "0 0 1,15 ? * /usr/bin/find"
        with self.assertRaises(ValueError) as context:
            parse_cron_string(cron_string)
        self.assertIn("Invalid month field: month='?'", str(context.exception))

    def test_both_day_of_month_and_day_of_week_question_mark(self):
        cron_string = "0 0 ? * ? /usr/bin/find"
        with self.assertRaises(ValueError) as context:
            parse_cron_string(cron_string)
        self.assertIn("Day of the Month and Day of the Week fields can not be `?` at the same time", str(context.exception))

    def test_not_implemented_day_of_month_w_and_l(self):
        cron_string = "0 0 1W * 1-5 /usr/bin/find"
        with self.assertRaises(NotImplementedError) as context:
            parse_cron_string(cron_string)
        self.assertIn("`W` and `L` are not yet supported for day_of_month", str(context.exception))

    def test_not_implemented_day_of_week_l_and_hash(self):
        cron_string = "0 0 1,15 * 1L /usr/bin/find"
        with self.assertRaises(NotImplementedError) as context:
            parse_cron_string(cron_string)
        self.assertIn("`L` and `#` are not yet supported for day_of_week", str(context.exception))


class TestGetTimeFields(unittest.TestCase):
    def test_wildcard(self):
        self.assertEqual(get_time_fields("*", 59, 0), list(range(0, 60)))
        self.assertEqual(get_time_fields("?", 59, 0), list(range(0, 60)))

    def test_single_value(self):
        self.assertEqual(get_time_fields("5", 59, 0), [5])
        self.assertEqual(get_time_fields("23", 23, 0), [23])

    def test_range(self):
        self.assertEqual(get_time_fields("1-5", 59, 0), [1, 2, 3, 4, 5])
        self.assertEqual(get_time_fields("10-15", 59, 0), [10, 11, 12, 13, 14, 15])

    def test_interval(self):
        self.assertEqual(get_time_fields("*/15", 59, 0), [0, 15, 30, 45])
        self.assertEqual(get_time_fields("5/10", 59, 0), [5, 15, 25, 35, 45, 55])

    def test_multiple_fields(self):
        self.assertEqual(get_time_fields("*,1-5", 59, 0), list(range(0, 60)))
        self.assertEqual(get_time_fields("1-5,*", 59, 0), list(range(0, 60)))

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            get_time_fields("invalid", 59, 0)
        with self.assertRaises(ValueError):
            get_time_fields("1-5-10", 59, 0)
        with self.assertRaises(ValueError):
            get_time_fields("*/", 59, 0)


class TestValidateTimeString(unittest.TestCase):

    def test_valid_time_string_with_asterisk(self):
        self.assertTrue(validate_time_string("*", 59))

    def test_valid_time_string_with_range(self):
        self.assertTrue(validate_time_string("0-59", 59))

    def test_valid_time_string_with_list(self):
        self.assertTrue(validate_time_string("0,15,30,45", 59))

    def test_valid_time_string_with_interval(self):
        self.assertTrue(validate_time_string("*/15", 59))

    def test_invalid_time_string_with_out_of_range_value(self):
        self.assertFalse(validate_time_string("0-60", 59))

    def test_invalid_time_string_with_invalid_character(self):
        self.assertFalse(validate_time_string("0-5a", 59))

    def test_invalid_time_string_with_invalid_interval(self):
        self.assertFalse(validate_time_string("*/a", 59))

if __name__ == '__main__':
    unittest.main()