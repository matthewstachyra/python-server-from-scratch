'''python server from scratch'''
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket option - you specify the socket option name as well as the level. Here
# we are at the SOL_SOCKET level and setting the option SO_REUSEADDR to be true, which
# means that bind will "permit the resuse of local addresses for this socket." So you can
# have two sockets with the same Internet port number
# https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print(f"Serving http on port {PORT}")
while True:
    connection, address = listen_socket.accept()
    data = connection.recv(1024)
    print(data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # http_response = b"""\
    # HTTP/1.1 200 OK
    # Hello World!"""

    connection.sendall(http_response)
    connection.close()

# import socket

# HOST, PORT = '', 8888

# listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# listen_socket.bind((HOST, PORT))
# listen_socket.listen(1)
# print(f'Serving HTTP on port {PORT} ...')
# while True:
#     client_connection, client_address = listen_socket.accept()
#     request_data = client_connection.recv(1024)
#     print(request_data.decode('utf-8'))

#     http_response = b"""\
# HTTP/1.1 200 OK

# Hello, World!
# """
#     client_connection.sendall(http_response)
#     client_connection.close()
