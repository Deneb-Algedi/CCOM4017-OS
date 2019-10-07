from random import randint
import socket 
import sys
from time import sleep

#program input: id, host & port
mobileID = str(sys.argv[1]) 
host = sys.argv[2] 
port = int(sys.argv[3])


#random number of jobs ---> CAN BE ASSIGNED BY USER <----
numJobs = randint(1,9)
#random MAX cpu time ---> CAN BE ASSIGNED BY USER <----
maxTime = randint(1,5)

#array for random cpu time
jobs = [0] * numJobs

#assign random cpu time for job
for i in range(numJobs):
    jobs[i] = randint(1,maxTime)


#create udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#server's ip & port
server_address = (host, port)

#sending messages with "Mobile ID:job cpu time"
for i in range(numJobs):
    message = mobileID + ":" + str(jobs[i])

    try:

        # Send data
        print ('Sending "%s"' % message)
        send = sock.sendto(message, server_address)
        print ('Message sent')
        
        #sleep random period of time between sends
        sleep(randint(1,5))

    except:
         print('Error sending message')


#close socket
print ('Closing socket')
sock.close()
