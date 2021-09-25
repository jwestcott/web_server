from typing import Tuple, Dict, List

from BaseHTTPParser import BaseHTTPParser
from HTTPRequest import HTTPRequest


class SplitterHTTPParser(BaseHTTPParser):

    @staticmethod
    def parse(http_byte_set: bytes) -> HTTPRequest:
        """Implements the HTTPParser through the use of the inbuilt split command to separate the incoming bytestream"""
        http_lines = http_byte_set.split(b"\r\n")
        http_method, http_uri, http_version = SplitterHTTPParser._extract_first_line(http_lines[0])
        http_headers = SplitterHTTPParser._extract_headers(http_lines[1:-2])
        data = http_lines[-1]
        return HTTPRequest(http_method, http_uri, http_version, http_headers, data)

    @staticmethod
    def _extract_first_line(http_first_line: bytes) -> Tuple[str, str, str]:
        http_first_line_string = http_first_line.decode("ASCII")
        http_fields = http_first_line_string.split(" ")
        http_method, http_uri, http_version = http_fields
        return http_method, http_uri, http_version

    @staticmethod
    def _extract_headers(http_headers: List[bytes]) -> Dict[str, str]:
        http_header_dict = {}
        for header_pair in http_headers:
            header_pair_str = header_pair.decode("ASCII")
            header_pair_split = header_pair_str.split(": ")
            http_header_dict[header_pair_split[0]] = "".join(header_pair_split[1:])
        return http_header_dict


if __name__ == "__main__":
    message = b'POST / HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.67.0\r\nAccept: */*\r\nContent-Length: 4\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\ntest'
    print(SplitterHTTPParser.parse(message))
