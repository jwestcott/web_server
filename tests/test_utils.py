import unittest
from datetime import timezone, datetime, tzinfo, timedelta
from typing import Optional

from vulcan.utils import TimestampMixin


class MockTimezone(tzinfo):

    def __init__(self, offset: int):
        self.offset = timedelta(hours=offset)

    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return self.offset

    def dst(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return timedelta(0)


class TestTimestampMixin(unittest.TestCase):

    def setUp(self) -> None:
        self.test_object = TimestampMixin()

    def tearDown(self) -> None:
        TimestampMixin.set_timezone(timezone.utc)

    def test_init_method_produces_timestamp_in_class_timezone(self) -> None:
        test_datetime = self.test_object.get_timestamp()
        self.assertIsInstance(test_datetime, datetime)
        self.assertEqual(test_datetime.tzinfo, TimestampMixin.TIMEZONE)

    def test_passed_datetime_is_converted_to_class_timezone_if_passed_datetime_is_in_different_timezone(self) -> None:
        different_timezone = MockTimezone(-1)
        passed_datetime = datetime.now(tz=different_timezone)
        self.test_object.set_timestamp(passed_datetime)
        result_timestamp = self.test_object.get_timestamp()
        self.assertNotEqual(passed_datetime.tzinfo, result_timestamp.tzinfo)
        self.assertEqual(result_timestamp.tzinfo, TimestampMixin.TIMEZONE)

    def test_held_datetime_is_converted_to_class_timezone_if_class_timezone_is_changed(self) -> None:
        different_timezone = MockTimezone(-1)
        TimestampMixin.set_timezone(different_timezone)
        result_timestamp = self.test_object.get_timestamp()
        self.assertEqual(result_timestamp.tzinfo, TimestampMixin.TIMEZONE)


if __name__ == "__main__":
    unittest.main()
