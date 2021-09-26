from datetime import datetime, timezone, tzinfo
from typing import Dict


class BaseRequest:
    """
    Base class for all incoming request types.

    This class predominantly adds a timestamp to an incoming request. By default the timestamp is the current time in
    the UTC timezone. This behaviour can however be overridden to support any timezone that extends the datetime.tzinfo
    class.
    """

    TIMEZONE: tzinfo = timezone.utc

    def __init__(self, timestamp: datetime = None) -> None:
        if timestamp is None:
            self._timestamp = datetime.now(self.TIMEZONE)
        else:
            self._timestamp = timestamp.astimezone(self.TIMEZONE)

    def get_timestamp(self) -> datetime:
        self._timestamp = self._timestamp.astimezone(self.TIMEZONE)
        return self._timestamp

    def set_timestamp(self, timestamp: datetime) -> None:
        self._timestamp = timestamp.astimezone(self.TIMEZONE)

    @classmethod
    def set_all_timezone(cls, timezone: tzinfo) -> None:
        cls.TIMEZONE = timezone















class HTTPRequest(BaseRequest):
    """Class for keeping track of HTTP request information"""

    def __init__(self, method: str, uri: str, http_version: str, headers: Dict[str, str], data: bytes,
                 timestamp: datetime = None):
        super().__init__(timestamp=timestamp)
        self.method = method
        self.uri = uri,
        self.http_version = http_version
        self.headers = headers
        self.data = data


if __name__ == "__main__":
    a = BaseRequest()
    print(a)