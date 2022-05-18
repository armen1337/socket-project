import socket

import config
from server.base_server import BaseServer


class Host(BaseServer):
    @BaseServer._socket_initializer
    def run_server(self, quiet: bool = True):
        self._sock.bind((self._host, self._port))
        self._sock.listen()

        while True:
            conn, address = self._sock.accept()

            with conn:
                print("Connection from:", address)
                
                msg = conn.recv(4096)
                
                if msg.decode().lower().strip() in ["destroy", "exit", "quit", "q"]:
                    break
                
                if not quiet:
                    print(msg.decode())

                conn.sendall(msg)
