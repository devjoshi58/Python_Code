from multiprocessing import Process,Value,Array,Lock, process
from multiprocessing import Queue
import time

def square(numbers,queue):

    for i in numbers:
        queue.put(i*i)
    
def make_negative(numbers,queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":

    q = Queue()
    numbers = range(0,5)
    process1 = Process(target=square,args=(numbers,q))
    process2 = Process(target=make_negative,args=(numbers,q))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    while not q.empty():
        print(q.get())



