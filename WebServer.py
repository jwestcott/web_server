from dataclasses import dataclass
import socket


class SocketFactory:

    @staticmethod
    def get_socket(port: int) -> socket.socket:
        """Returns a Socket Object configured to listen on the passed port"""
        return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return_socket.bind(("", port))
        return return_socket


@dataclass
class HTTPRequest:
    """Class for keeping track of HTTP request information"""
    return_ip: str
    return_port: int
    method: str
    url: str
    http_version: str
    headers: dict
    data: str


class HTTPParser:

    @staticmethod
    def parse_request(request: bytes) -> HTTPRequest:
        request_str = request.decode("ASCII")
        request_split = request_str.split("\r\n")
        method, url, http_version = request_split[0].split(" ")
        return HTTPRequest(method, url, http_version, {"test": "test"}, "DATA")


class WebServer:

    def __init__(self, port=8080) -> None:
        self.port = port
        self.server_socket = SocketFactory.get_socket(port)

    def start(self) -> None:
        self.server_socket.listen()
        while True:
            connection, ipaddress = self.server_socket.accept()
            test = connection.recv(2048)
            request = HTTPParser.parse_request(test)
            print(request)


if __name__ == "__main__":
    a = WebServer(port=8080)
    a.start()
