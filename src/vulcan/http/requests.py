from datetime import datetime, timezone, tzinfo
from typing import Dict

from vulcan.utils import TimestampMixin

class BaseRequest(TimestampMixin):
    """
    Base class for all request objects. Uses the TimestampMixin to provide timestamp capabilities.
    """

    def __init__(self):
        super().__init__()


class HTTPRequest(BaseRequest):
    """
    Data class for keeping track of HTTP request information.
    """

    def __init__(self, method: str, uri: str, http_version: str, headers: Dict[str, str], data: bytes):
        super().__init__()
        self.method = method
        self.uri = uri
        self.http_version = http_version
        self.headers = headers
        self.data = data

    def __repr__(self) -> str:
        return "HTTPRequest(http_version={}, method={}, uri={})".format(self.http_version, self.method, self.uri)
