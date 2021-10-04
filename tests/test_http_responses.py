import unittest

from vulcan.http.responses import HTTPResponse


class TestHTTPResponse(unittest.TestCase):

    def setUp(self) -> None:
        self.testResponse = HTTPResponse()

    def test_HTTPResponse_serialize_correctly_serializes_a_response_with_no_data_and_no_headers(self) -> None:
        self.testResponse.http_version = "HTTP/1.1"
        self.testResponse.status_code = 200
        self.testResponse.phrase = "OK"
        result = self.testResponse.serialize()
        self.assertEqual(b"HTTP/1.1 200 OK\r\n\r\n", result)

    def test_HTTPResponse_serialize_correctly_serializes_a_response_with_headers_but_no_data(self) -> None:
        self.testResponse.http_version = "HTTP/1.1"
        self.testResponse.status_code = 200
        self.testResponse.phrase = "OK"
        self.testResponse.headers = {"test": "case"}
        result = self.testResponse.serialize()
        self.assertEqual(b"HTTP/1.1 200 OK\r\ntest: case\r\n\r\n", result)

    def test_HTTPResponse_serialize_correctly_serializes_a_response_with_headers_and_data(self) -> None:
        self.testResponse.http_version = "HTTP/1.1"
        self.testResponse.status_code = 200
        self.testResponse.phrase = "OK"
        self.testResponse.headers = {"test": "case"}
        self.testResponse.data = b"test data"
        result = self.testResponse.serialize()
        self.assertEqual(b"HTTP/1.1 200 OK\r\ntest: case\r\n\r\ntest data", result)


if __name__ == "__main__":
    unittest.main()