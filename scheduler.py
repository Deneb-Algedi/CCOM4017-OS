import socket
import sys
import threading
from time import sleep

#number of jobs ---> CAN BE ASSIGNED BY USER <----
N = 10
#count jobs 
jobs = N

#control access to critical region
lock = threading.Semaphore()
#empty slots
empty = threading.Semaphore(N)
#full slots
full = threading.Semaphore(0)


#Queue to hold messages
scheduler = []
#Dictionary for cpu time of each mobile
dic = {}

#server address & port
host = 'localhost'
port = int(sys.argv[1])

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (host, port)
print ('Starting up on %s port %s' % server_address)
sock.bind(server_address)

def producer():
    global jobs

    while (jobs):
        #await client message
        print ('Waiting to receive message')
        recv = sock.recvfrom(port)
        msg = recv[0]
        
        #no data received 
        if not msg:
            break
        
        #critical region 
        empty.acquire()
        lock.acquire()
        print ('Adding ' + msg + ' to queue.')
        #add msg to queue
        scheduler.append(msg)
        lock.release()
        full.release()

def consumer():
    global jobs

    while (jobs):
        #critical region
        full.acquire()
        lock.acquire()
        mobile_id, time = scheduler.pop().split(":")
        #substract for remaining jobs
        jobs -= 1
        lock.release()
        empty.release() 

        #insert mobile id in dic and add up its time
        if (mobile_id in dic):
            dic[mobile_id] += int(time)
        else:
            dic[mobile_id] = int(time)

        #sleep time amount
        sleep(int(time))

    #display cpu time results 
    for key, value in dic.items():
        print("Mobile " + key + " consumed " + str(value) + " CPU time.")
            

#create threads
producer_thread = threading.Thread(target = producer)
consumer_thread = threading.Thread(target = consumer)
#start threads
producer_thread.start()
consumer_thread.start()
#wait for thread
producer_thread.join()
consumer_thread.join()


#close socket
print ('Closing socket')
sock.close()
