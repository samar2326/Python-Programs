queue=["cat","dog","eagle","fan"]
print("queue:", queue)
queue.insert(0,"boy")
queue.insert(0,"apple")
print("New_queue:",queue)
print("Deleted item:",queue.pop())
print(queue)
print("Deleted item:",queue.pop())
print(queue)




#----------------  method 2 ----------------------

from collections import deque
queue=deque(["apple","banana","cucumber"])
print(queue)
queue.append("rose")
queue.append("lily")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
