import socket
import sys

# source :https://pymotw.com/2/socket/tcp.html
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        data=""

        data = data+connection.recv(2000)
        print >>sys.stderr, 'received "%s"' % data
        connection.sendall("A")
        print >>sys.stderr, 'sending Ack to the client'
        connection.sendall("A")

    finally:
        # Clean up the connection
        connection.close()
