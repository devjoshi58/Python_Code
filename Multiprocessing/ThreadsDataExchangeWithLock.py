#Exchanging data between threads
#Example of using lock so that same value is not changed by multiple threads

from threading import Thread,Lock
import time

database_Value = 0

def increase(lock):
    lock.acquire()
    global database_Value

    local_value = database_Value

    local_value+=1
    time.sleep(0.1)
    database_Value=local_value
    lock.release()

if __name__ == "__main__":

    print("starting value",database_Value)
    lock = Lock()
    thread1 = Thread(target=increase,args=(lock,)) #Argument is a tuple hence we use , to define tuple with single element
    thread2 = Thread(target=increase,args=(lock,)) 
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"End value {database_Value}")
    








