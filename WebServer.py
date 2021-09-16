import socket

from HTTPRequest import HTTPRequest
from SplitterHTTPParser import SplitterHTTPParser


class SocketFactory:

    @staticmethod
    def get_socket(port: int) -> socket.socket:
        """Returns a Socket Object configured to listen on the passed port"""
        return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return_socket.bind(("", port))
        return return_socket


class WebServer:

    def __init__(self, port=8080) -> None:
        self.port = port
        self.server_socket = SocketFactory.get_socket(port)

    def start(self) -> None:
        self.server_socket.listen()
        while True:
            connection, ipaddress = self.server_socket.accept()
            incoming_bytes = connection.recv(2048)
            http_request = SplitterHTTPParser.parse(incoming_bytes)
            print(http_request)


if __name__ == "__main__":
    a = WebServer(port=8080)
    a.start()
