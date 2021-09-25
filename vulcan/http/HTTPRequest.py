from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class HTTPRequest:
    """Class for keeping track of HTTP request information"""
    method: str
    uri: str
    http_version: str
    headers: Dict[str, str]
    data: bytes
    request_timestamp: datetime = field(default=datetime.now())
 