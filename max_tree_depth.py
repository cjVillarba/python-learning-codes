class Node():
	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None
		
	def max_height(root):
		if not root:
			return 0
		height = 0
		queue = [root]
		while queue:
			height += 1
			level = []
			while queue:
				node = queue.pop()
				if node.left:
					level.append(node.left)
				if node.right:
					level.append(node.right)
			queue = level
		return height
	
	def print_tree(self):
		if self:
			print(self.val)
			self.print_tree(self.left)
			self.print_tree(self.right)

tree = Node(10)
tree.left = Node(12)
tree.right = Node(15)

height = tree.max_height()
trees = tree.print_tree()

print(trees)
print("Height :", height)