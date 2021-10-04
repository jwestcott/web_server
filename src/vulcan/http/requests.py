from typing import Dict

from vulcan.http.serializers import Serializable, serlialize_http_headers
from vulcan.utils import TimestampMixin

class BaseRequest(TimestampMixin):
    """
    Base class for all request objects. Uses the TimestampMixin to provide timestamp capabilities.
    """

    def __init__(self):
        super().__init__()


class HTTPRequest(BaseRequest, Serializable):
    """
    Data class for keeping track of HTTP request information.
    """

    def __init__(self,
                 method: str = "GET",
                 uri: str = "/",
                 http_version: str = "HTTP/1.1",
                 headers: Dict[str, str] = {},
                 data: bytes = None
                 ):
        super().__init__()
        self.method = method
        self.uri = uri
        self.http_version = http_version
        self.headers = headers
        self.data = data

    def serialize(self) -> bytes:
        """
        Serializes the HTTP Request to a bytes object.

        :return: A bytes object representing the HTTPRequest object
        """
        request_line = b" ".join([x.encode("ASCII") for x in [self.method, self.uri, self.http_version]]) + b"\r\n"
        header_lines = serlialize_http_headers(self.headers)
        data_lines = b"" if self.data is None else self.data
        return request_line + header_lines + b"\r\n" + data_lines

    def __repr__(self) -> str:
        return "HTTPRequest(http_version={}, method={}, uri={})".format(self.http_version, self.method, self.uri)
