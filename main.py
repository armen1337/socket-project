import config

from server.client import Client
from server.host import Host


if __name__ == "__main__":
    host = Host(config.HOST, config.PORT)
    host.run_server(quiet=False)

