import socket

import config
from utils.exceptions import ConnectionRequiredException


class BaseServer:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._sock = None
    
    def get_host(self):
        return self._host
    
    def get_port(self):
        return self._port

    def _requires_sock(func):
        def wrapper(self, *args, **kwargs):
            if self._sock is None:
                raise ConnectionRequiredException("Connection is required! Make sure you called the appropriate method before interaction.")
            func(self, *args, **kwargs)

        return wrapper
    
    def _initialize_socket(self):
        if self._sock is None:
            self._sock = socket.socket(config.ADDRESS_FAMILY, config.SOCKET_TYPE)

    def _socket_initializer(func):
        def wrapper(self, *args, **kwargs):
            self._initialize_socket()
            func(self, *args, **kwargs)

        return wrapper
