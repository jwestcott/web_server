from abc import ABC, abstractmethod
from typing import Dict

class Serializable(ABC):
    """
    Base abstract class (interface) to provide serializable functionality to implementing classes.
    """

    @abstractmethod
    def serialize(self) -> bytes:
        """
        Abstract method that represents a serialization operation to a bytes object. Needs to be implemented in classes
        that extend the base Serializable class.

        :return: The serialized result as a bytes object.
        """
        pass


def serlialize_http_headers(header_dict: Dict[str, str]) -> bytes:
    """
    Serializes a dictionary containing HTTP headers into a bytes object

    :param header_dict: A dictionary containing key value pairs of HTTP headers
    :return: a bytes object representing the serialized HTTP headers
    """
    if len(header_dict) == 0:
        return b""
    else:
        return_bytes = b""
        for header_key, header_value in header_dict.items():
            return_bytes += "{}: {}\r\n".format(header_key, header_value).encode("ASCII")
        return return_bytes


class Parseable(ABC):
    """
    Base Abstract class (interface) that indicates a class can be parsed.
    """
    pass


class BaseParser(ABC):
    """
    Base Abstract class (interface) for parsing parseable objects.
    """

    @abstractmethod
    def parse(self, input_bytes_object: bytes) -> Parseable:
        pass
