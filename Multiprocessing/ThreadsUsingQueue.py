from threading import Thread,Lock,current_thread
from queue import Queue
import time

def worker(q,lock):
    while True:
        value = q.get()
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 7

    for i in range(num_threads):
        thread = Thread(target=worker,args=(q,lock))
        Thread.daemon = True #Threads that are daemons, however, are just killed wherever they 
                                #are when the program is exiting.


        thread.start()
    
    for i in range(1,25):
        q.put(i)
    
    q.join() #To tell one thread to wait for another thread to finish, you call .join().

    print("end main")

