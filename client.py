import socket
import time

s = socket.socket()
s.connect(('localhost',1999))
total=20480
print ("total data size: "+str(total))
for j in  [2,4,5,8,10,16,20,32,40,80]:
 times=j
 a=time.time()

 mlen=total/j
 for i in range(times):                  # Send integers from 0 to 9

    z=str(j)*(mlen)
    s.sendall(z)
    d1=s.recv(20480)
    # print("Client Received")
    # print(d1)

 b=time.time()
 print("message size :"+ str(mlen))

 print ("Number of messages:" +str(times))

 print("time took  :"+ str(b-a))
s.close()
