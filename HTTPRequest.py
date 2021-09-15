from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class HTTPRequest:
    """Class for keeping track of HTTP request information"""
    method: str
    url: str
    http_version: str
    headers: dict
    data: bytes
    request_timestamp: datetime = field(default=datetime.now())
