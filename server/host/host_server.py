import socket

import config
from utils import Logger
from server.base_server import BaseServer


class Host(BaseServer):
    @BaseServer._socket_initializer
    def run_server(self) -> None:
        try:
            self._sock.bind((self._host, self._port))
            Logger.info(f"Server started at http://{self._host}:{self._port}")
        except socket.gaierror:
            Logger.exception("socket.gaierror -> Invalid host or port")
            return

        self._sock.listen()
        self._handle_client_requests()

    def _handle_client_requests(self):
        while True:
            self._conn, self._address = self._sock.accept()

            with self._conn:
                Logger.info("Connection from:", self._address)
                msg = self._conn.recv(50 * 1024)

                if msg.decode().lower().strip() in ["destroy", "exit", "quit", "q"]:
                    break

                self._serve_files(msg)

    def _serve_files(self, msg: bytes):
        msg_utf8 = msg.decode('utf-8').split('\r\n')
        print(msg_utf8)
        header = 'HTTP/1.1 200 OK\n'
        filename = msg_utf8[0].split(" ")[1].lstrip("/")
        filename = filename if filename != '' else 'index.html'

        try:
            with open(config.FRONTENDS_FOLDER + filename, 'rb') as f:
                response = f.read()
        except FileNotFoundError:
            with open(config.FRONTENDS_FOLDER + "index.html", 'rb') as f:
                response = f.read()
                print(response)

        if filename.endswith(".jpg"):
            mimetype = 'image/jpg'
        elif filename.endswith(".css"):
            mimetype = 'text/css'
        elif filename.endswith(".js"):
            mimetype = 'text/javascript'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: ' + str(mimetype) + '\n\n'

        self._conn.sendall(header.encode() + response)
