from collections import deque

class Queue:
	
	def __init__(self):
		self._queue = deque([])
		
	def add(self, value):
		self._queue.append(value)
		
	def remove(self):
		return self._queue.popleft()
		
	def is_empty(self):
		return not len(self._queue)
		
	def size(self):
		return len(self._queue)

#print(dir(collections))

new_q = Queue()
new_q.add(1)
new_q.add(2)
new_q.add(3)
print(new_q.size())
print(new_q._queue)

rem = new_q.remove()
print(rem)

print(new_q.is_empty())