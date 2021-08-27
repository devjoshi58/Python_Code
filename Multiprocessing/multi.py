#Multiprocessing

from multiprocessing import Process

import os
import time 

def squarenum():

    for i in range(10):
        i*i
        time.sleep(0.5)

if __name__ == "__main__":
    processes = []
    numprocess = os.cpu_count()

    #create processes

    for i in range(numprocess):
        p = Process(target=squarenum)  #create a process
        processes.append(p) # append the process to the process list

    #start the process

    for p in processes:
        p.start()

    #join to make sure all processes are completed

    for p in processes:
        p.join()

    print('end main')

