from queue import Queue

q = Queue()

q.put(1)
q.put(2)

first = q.get()
print(first)
q.task_done() #to notify that we are done processing this and can continue
q.join() #blocks main thread until all elements have been processed

 