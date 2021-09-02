from multiprocessing import Process,Lock,Value,Array


def add_100(numbers,lock):
    for i in range(100):
        with lock:
            for j in range(len(numbers)):
                numbers[j]+=1


if __name__ == "__main__":

    lock = Lock()
    shared_array = Array('d',[1,2,3])
    print("shared array beginning value",shared_array[:])

    p1 = Process(target=add_100,args=(shared_array,lock)) #args is a tuple
    p2 = Process(target=add_100,args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("shared array end value",shared_array[:])


