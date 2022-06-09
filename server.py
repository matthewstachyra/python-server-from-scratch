'''python server from scratch'''
import socket

# any 4 positive integers. Ports <1000 are typically reserved so you will run into issues.
PORT = 8888

# create socket - first parameter (socket.AF_INET) specifies that this is
# ipv4 ip address where AF stands for address family and INET represents ipv4
# and the second parameter specifies it is a TCP or transmission control protocol
# socket, or a streaming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket option - you specify the socket option name as well as the level. Here
# we are at the SOL_SOCKET level and setting the option SO_REUSEADDR to be true, which
# means that bind will "permit the resuse of local addresses for this socket." So you can
# have two sockets with the same Internet port number
# NOTE: this socket option is not strictly necessary
# https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# a socket is just an endpoint for some communication. It is an ip address and a port. Since
# this server is local, the hostname is whatever the local hostname is.
s.bind((socket.gethostname(), PORT))

# prepares the socket to listen and gives a queue of 5.
s.listen(5)

# we use a while loop because we are listening forever.
print(f"Serving http on port {PORT} ... ")
while True:
    # if someone connects to the socket, we will automatically accept them. The connection is the client
    # that is connecting and the address is where are they coming from, so basically their IP.
    connection, address = s.accept()
    print(f"Connection from {address} established.")

    # recieve information from the connection with a buffer size of 1024
    data = connection.recv(1024)

    # print out what information was recieved as a decoded byte string (because the message) is entered
    # as a utf-8 encoded byte string
    print(data.decode('utf-8'))

    http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """

    connection.sendall(http_response)
    connection.close()

