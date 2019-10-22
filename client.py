import socket
import sys
import time
# reference :https://pymotw.com/2/socket/tcp.html

# Create a TCP/IP et
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the et to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    # Send data
    message = 'a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the serverSocket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the serverSocket=ient reaches out to the serverSocker. , while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the serverSocket programming is a way of connecting two nodes on a network to communicate with each other. One on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the serveruu'
    print ("sending data of size: "+str(sys.getsizeof(message)))
    sent_time = int(round(time.time() * 1000))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    data=""


