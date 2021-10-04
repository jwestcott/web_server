from typing import Dict

from vulcan.http.serializers import Serializable, serlialize_http_headers, Parseable, BaseParser
from vulcan.utils import TimestampMixin

class BaseResponse(TimestampMixin):
    """
    Base class for all response objects. Uses the TimestampMixin to provide timestamp capabilitites.
    """

    def __init__(self):
        super().__init__()


class HTTPResponse(BaseResponse, Serializable, Parseable):
    """
    Data class for keeping track of HTTP response information.
    """

    DEFAULT_REASON_PHRASES = {
        100: "Continue",
        101: "Switching Protocols",
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        307: "Temporary Redirect",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Forbidden",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Time-out",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Request Entity Too Large",
        414: "Request-URI Too Large",
        415: "Unsupported Media Type",
        416: "Requested range not satisfiable",
        417: "Expectation Failed",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Time-out",
        505: "HTTP Version not supported"
    }


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
        self.phrase = self.DEFAULT_REASON_PHRASES[self.status_code] if phrase is None else phrase
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


class HTTPResponseParser(BaseParser):

    def parse(self, input_bytes_object: bytes) -> HTTPResponse:
        pass
