import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',1999))
s.listen(3)

print ('Server is listening')

while True:
    c, addr = s.accept()

    print ('Connection from ', addr)
    print("Client Sent")
    d=c.recv(20480)
    # d=str(int(d[0])+1)
    c.sendall("1")
c.close()
