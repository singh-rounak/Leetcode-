#Given a binary tree, find the level in the tree where the sum of all nodes on that level is the greatest.
from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return "(Value: {} Left: {} Right: {})".format(self.value,self.left,self.right)


def tree_level_max_sum(root):
  if not root:
  	return

  sum_ = 0
  queue = deque()
  queue.append(root)
  MaxSum = root.value


  while len(queue)>0:

  	temp = queue.popleft()
  	sum_+= temp.value

  	if temp.left:
  		queue.append(temp.left)
  	if temp.right:
  		queue.append(temp.right)

  	MaxSum = max(sum_, MaxSum)

  return MaxSum





n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum
