from typing import Dict

from vulcan.http.serializers import Serializable, serlialize_http_headers
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

    def __init__(self,
                 http_version: str = "HTTP/1.1",
                 status_code: int = 200,
                 phrase: str = "OK",
                 headers:Dict[str, str] = {},
                 data: bytes = None
                 ):
        super().__init__()
        self.http_version = http_version
        self.status_code = status_code
        self.phrase = phrase
        self.headers = headers
        self.data = data

    def serialize(self) -> bytes:
        """
        Serializes the HTTP Response to a bytes object.

        :return: A bytes object representing the HTTPResponse object
        """
        response_parameters = [self.http_version, str(self.status_code), self.phrase]
        response_line = b" ".join([x.encode("ASCII") for x in response_parameters]) + b"\r\n"
        header_lines = serlialize_http_headers(self.headers)
        data_lines = b"" if self.data is None else self.data
        return response_line + header_lines + b"\r\n" + data_lines

    def __repr__(self) -> str:
        return "HTTPResponse(http_version={}, status_code={}, phrase={})".format(self.http_version,
                                                                                 self.status_code,
                                                                                 self.phrase)
    