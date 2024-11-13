import socket
import socket_config as cfg

client_socket = socket.socket()
client_socket.connect((cfg.server, cfg.port))
