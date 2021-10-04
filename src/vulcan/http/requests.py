from typing import Dict, Tuple, List

from vulcan.http.serializers import Serializable, serlialize_http_headers, Parseable, BaseParser
from vulcan.utils import TimestampMixin

class BaseRequest(TimestampMixin):
    """
    Base class for all request objects. Uses the TimestampMixin to provide timestamp capabilities.
    """

    def __init__(self):
        super().__init__()


class HTTPRequest(BaseRequest, Serializable, Parseable):
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


class HTTPRequestParser(BaseParser):

    def parse(self, http_byte_set: bytes) -> HTTPRequest:
        """
        Implements the HTTPParser through the use of the inbuilt split command to separate the incoming bytestream.
        """
        http_lines = http_byte_set.split(b"\r\n")
        http_method, http_uri, http_version = self._extract_first_line(http_lines[0])
        http_headers = self._extract_headers(http_lines[1:-2])
        data = http_lines[-1]
        return HTTPRequest(
            method = http_method,
            uri = http_uri,
            http_version = http_version,
            headers = http_headers,
            data = data
        )

    def _extract_first_line(self, http_first_line: bytes) -> Tuple[str, str, str]:
        http_first_line_string = http_first_line.decode("ASCII")
        http_fields = http_first_line_string.split(" ")
        http_method, http_uri, http_version = http_fields
        return http_method, http_uri, http_version

    def _extract_headers(self, http_headers: List[bytes]) -> Dict[str, str]:
        http_header_dict = {}
        for header_pair in http_headers:
            header_pair_str = header_pair.decode("ASCII")
            header_pair_split = header_pair_str.split(": ")
            http_header_dict[header_pair_split[0]] = "".join(header_pair_split[1:])
        return http_header_dict

