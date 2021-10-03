from typing import Dict

from vulcan.http.serializers import Serializable
from vulcan.utils import TimestampMixin

class BaseResponse(TimestampMixin):
    """
    Base class for all response objects. Uses the TimestampMixin to provide timestamp capabilitites.
    """

    def __init__(self):
        super().__init__()


class HTTPResponse(BaseResponse, Serializable):
    """
    Data class for keeping track of HTTP response information.
    """

    def __init__(self, http_version: str, status_code: int, phrase: str, headers:Dict[str, str], data: bytes):
        super().__init__()
        self.http_version = http_version
        self.status_code = status_code
        self.phrase = phrase
        self.headers = headers
        self.data = data

    def serialize(self) -> bytes:
        pass

    def __repr__(self) -> str:
        return "HTTPResponse(http_version={}, status_code={}, phrase={})".format(self.http_version,
                                                                                 self.status_code,
                                                                                 self.phrase)
