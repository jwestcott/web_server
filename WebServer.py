import socket

from vulcan.http.requests import HTTPRequestParser
from vulcan.http.responses import HTTPResponse


class SocketFactory:

    @staticmethod
    def get_socket(port: int) -> socket.socket:
        """Returns a Socket Object configured to listen on the passed port"""
        return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return_socket.bind(("", port))
        return return_socket


class WebServer:

    HTTP_PARSER = HTTPRequestParser()

    def __init__(self, port=8080) -> None:
        self.port = port
        self.server_socket = SocketFactory.get_socket(port)

    def start(self) -> None:
        self.server_socket.listen()
        while True:
            connection, ipaddress = self.server_socket.accept()
            incoming_bytes = connection.recv(2048)
            http_request = self.HTTP_PARSER.parse(incoming_bytes)
            print(http_request)
            http_response = HTTPResponse(headers={"Content-Type": "text/html"}, data=b"<h1>HELLO JONATHAN</h1>")
            connection.send(http_response.serialize())


if __name__ == "__main__":
    a = WebServer(port=8080)
    a.start()
