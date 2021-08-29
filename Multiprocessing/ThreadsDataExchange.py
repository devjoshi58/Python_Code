#Exchanging data between threads
#Example of Race condition when two threads update single value almost simultaneously

from threading import Thread
import time

database_Value = 0

def increase():
    global database_Value

    local_value = database_Value

    local_value+=1
    time.sleep(0.1)
    database_Value=local_value

if __name__ == "__main__":

    print("starting value",database_Value)
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"End value {database_Value}")
    #Result here is 1 as during the time.sleep the program starts the second thread and hence the local value goes back
    # to 0 and then becomes  1 again.








