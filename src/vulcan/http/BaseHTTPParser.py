from vulcan.http.HTTPRequest import HTTPRequest


class BaseHTTPParser:

    @staticmethod
    def parse(http_byte_set: bytes) -> HTTPRequest:
        """Parses an input byte set and returns a HTTPRequest object"""
        pass
