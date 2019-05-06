class Node:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
		
	def set_data(self,data):
		self.data = data
		
	def get_data(self):
		return self.data
	
	def set_next(self,next):
		self.next = next
		
	def get_next(self):
		return self.next
		
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
		
	def add(self, value):
		node = Node(value)
		node.set_next(self.head)
		self.head = node
		self.size += 1
	
	def _search_node(self,value,remove=False):
		current = self.head
		previous = None
		
		while current:
			if current.data == value:
				break
			else:
				previous = current
				current = current.next
		if remove and current:
			if previous is None:
				self.head = current.next
			else:
				previous.set_next(current.next)
			self.size -= 1
		
		return current is not None
	
	def remove(self,value):
		return self._search_node(value,True)
		
	def search(self,value):
		return self._search_node(value)
		
	def size(self):
		return self.size
		
new_sl = SinglyLinkedList()

new_sl.add(1)
new_sl.add(2)
new_sl.add(3)
new_sl.add("a")

print(new_sl)
print(new_sl.size)
print(new_sl.search(3))

new_sl.remove(2)
print(new_sl.size)
print(new_sl.search(2))

new_sl.remove(1)
new_sl.remove(3)
new_sl.remove("a")

print(new_sl.size)