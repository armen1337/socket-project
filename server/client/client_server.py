import socket

import config
from server.base_server import BaseServer


class Client(BaseServer):
    @BaseServer._socket_initializer
    def connect(self):
        self._sock.connect((self._host, self._port))

    @BaseServer._requires_sock
    def send_message(self, msg: bytes | str):
        if isinstance(msg, str):
            msg = msg.encode()
        
        self._sock.sendall(msg)
