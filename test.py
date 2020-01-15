import queue

a = queue.Queue()

a.put(1)
a.put(2)
a.put(3)

print(a.qsize())
print(a.queue)
print(a.qsize())

