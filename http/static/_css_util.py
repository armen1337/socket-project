import socket

from http._file_base_class import BaseFile


class CSSFile(BaseFile):
    def __new__(cls, filepath: str):
        BaseFile._verify_file_format(filepath, "css")
        return super().__new__(cls)

    def render(self, client_socket: socket.socket) -> None:
        client_socket.sendall(b"Content-Type: text/css\n\n"+self._contents.encode())
