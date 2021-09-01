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
    num_threads = 2

    for i in range(num_threads):
        thread = Thread(target=worker,args=(q,lock))
        Thread.daemon = True
        thread.start()
    
    for i in range(1,5):
        q.put(i)
    
    q.join() #lock the main thread and wait until all the items have been processed

    print("end main")

