from datetime import datetime, timezone


class TimestampMixin:
    """
    Abstract Mixin class for adding timestamp recording to child classes.

    Whenever an object deriving from this class is created, a timestamp variable is created in the form of a Python
    datetime object. By default the timestamp is the current UTC time. This behaviour can however be overridden to
    support any timezone that extends the datetime.tzinfo class. See the datetime documentation for more information.
    """

    TIMEZONE: tzinfo = timezone.utc

    @classmethod
    def set_timezone(cls, timezone: tzinfo) -> None:
        """
        Sets the class timezone to the passed timezone. This action will affect all instances of this class.

        :param timezone: The datetime.tzinfo object representing the desired timezone.
        """
        cls.TIMEZONE = timezone

    def __init__(self) -> None:
        """
        Creates a TimestampMixin object with a timestamp in the set timezone. By default this is in the UTC timezone.
        """
        self._timestamp = datetime.now(self.TIMEZONE)

    def get_timestamp(self) -> datetime:
        """
        Returns the timestamp as a datetime object.

        Each time the timestamp is retrieved, it is first converted to the timezone that is set at the class level (by
        default this is UTC). To avoid edgecases where changes to the timezone at the class level not reflecting in
        changes to the _timestamp class variable, it is recommended that all accesses to the timestamp come through
        this method.

        :return: datetime object representing the timestamp
        """
        self._timestamp = self._timestamp.astimezone(self.TIMEZONE)
        return self._timestamp

    def set_timestamp(self, timestamp: datetime) -> None:
        """
        Overwrites the stored timestamp to the

        :param timestamp:
        """
        self._timestamp = timestamp.astimezone(self.TIMEZONE)