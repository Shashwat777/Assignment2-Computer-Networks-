import socket
import time
import sys

total=20480 #Total data
print ("Total data size: "+str(total))
print("")

for j in  [2,4,5,8,10,16,20,32,40,80,160,64,128,256,516,1024]: #How many messages to send

   a=time.time()                           #start time
   times=j

   mlen=total/j                               #Each Message Length

   for i in range(times):                  # Send integers from 0 to 9
      s = socket.socket()
      s.connect(('localhost',1999))
      z=(str(j)[0])*(mlen)
      s.sendall(z)
      d1=s.recv(13000)
      # Ack
      # print("Ack  Received "+str(d1))
      # Ack validation , print false upon wrong  ack (for throughput)
      if(int(str(j)[0])+1!=int(d1)):
          print ("false")


      s.close()
   b=time.time()
   print("")
   print("Each Message size :"+ str(mlen))

   print ("Number of messages:" +str(times))

   print("Round-Trip Time(RTT)  :"+ str(b-a))
   print("")
