


class Node:
	data = 20
	next = None

	def __init__(self, data):
		self.data = data
		#self.next = next

	def __repr__(self):
		return "< Node data: %s >" % self.data

# N1 = Node(10)
# print(N1)

# N2 = Node(20)

# N1.next = N2

# print(N1.next)

class LinkedList:
	def __init__(self):
		self.head = None
		