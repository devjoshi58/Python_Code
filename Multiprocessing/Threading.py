#Multiprocessing

from threading import Thread

import os
import time 

def squarenum():

    for i in range(10):
        i*i
        time.sleep(0.5)

if __name__ == "__main__":
    threads = []
    numthreads = 10

    #create processes

    for i in range(numthreads):
        p = Thread(target=squarenum)  #create a process
        threads.append(p) # append the process to the process list

    #start the process

    for p in threads:
        p.start()

    #join to make sure all processes are completed

    for p in threads:
        p.join()

    print('end main')

