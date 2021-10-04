import unittest

from vulcan.http.requests import HTTPRequest


class TestHTTPRequest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_request = HTTPRequest()

    def test_HTTPRequest_serialize_correctly_serializes_a_request_with_no_headers_or_data(self) -> None:
        self.test_request.method = "TEST"
        self.test_request.uri = "/test/case"
        self.test_request.http_version = "HTTP/1.1"
        self.assertEqual(b"TEST /test/case HTTP/1.1\r\n\r\n", self.test_request.serialize())

    def test_HTTPRequest_serialize_correctly_serializes_a_request_with_no_headers_but_with_data(self) -> None:
        self.test_request.method = "TEST"
        self.test_request.uri = "/test/case"
        self.test_request.http_version = "HTTP/1.1"
        self.test_request.data = b"test data"
        self.assertEqual(b"TEST /test/case HTTP/1.1\r\n\r\ntest data", self.test_request.serialize())

    def test_HTTPRequest_serialize_correctly_serializes_a_request_with_headers_but_no_data(self) -> None:
        self.test_request.method = "TEST"
        self.test_request.uri = "/test/case"
        self.test_request.http_version = "HTTP/1.1"
        self.test_request.headers = {"test": "headers"}
        self.assertEqual(b"TEST /test/case HTTP/1.1\r\ntest: headers\r\n\r\n", self.test_request.serialize())


if __name__ == "__main__":
    unittest.main()
