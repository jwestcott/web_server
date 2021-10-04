import unittest

from vulcan.http.serializers import serlialize_http_headers


class TestSerializeHTTPHeaders(unittest.TestCase):

    def test_serialize_http_headers_returns_a_blank_bytes_object_if_an_empty_dictionary_is_passed(self):
        result = serlialize_http_headers({})
        self.assertEqual(b"", result)

    def test_serialize_http_headers_correctly_serializes_a_dictionary_with_a_single_entry(self):
        test_dict = {"test": "case"}
        result = serlialize_http_headers(test_dict)
        self.assertEqual(b"test: case\r\n", result)

    def test_serialize_http_headers_correctly_serializes_a_dictionary_with_multiple_entries(self):
        test_dict = {
            "test": "case",
            "another": "case"
        }
        result = serlialize_http_headers(test_dict)
        self.assertEqual(b"test: case\r\nanother: case\r\n", result)


if __name__ == "__main__":
    unittest.main()
