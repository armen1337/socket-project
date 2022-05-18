import config

from server.host import Host


if __name__ == "__main__":
    host = Host(config.HOST, config.PORT)
    host.run_server()

