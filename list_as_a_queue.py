from collections import deque
queue=deque (["python","ruby","java"])
print(queue)
queue.append("java")
print( queue)
print( queue.popleft())
print( queue)