from socket_project import config

from socket_project.server.host import Host


if __name__ == "__main__":
    host = Host(config.HOST, config.PORT)
    host.run_server()

