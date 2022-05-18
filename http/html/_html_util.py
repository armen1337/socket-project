import socket

from http._file_base_class import BaseFile


class HTMLFile(BaseFile):
    def __new__(cls, filepath: str):
        BaseFile._verify_file_format(filepath, "html")
        return super().__new__(cls)

    def render(self, client_socket: socket.socket) -> None:
        client_socket.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n"+self._contents.encode())
