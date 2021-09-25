from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass
class HTTPResponse:

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

    http_version: str
    status_code: int
    headers: Dict[str, str]
    data: bytes
    reason_phrase: str = field(default=None)
    response_timestamp: datetime = field(default=datetime.now())

    def to_bytes(self) -> bytes:
        status_line = "{} {} {}".format(self.http_version, self.status_code, self._get_reason_phrase())
        return bytes("hello")

    def _get_reason_phrase(self) -> str:
        pass

