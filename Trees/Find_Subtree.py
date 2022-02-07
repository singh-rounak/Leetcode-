
#Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same. 
#Return True if it exists, otherwise return False

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return "(Value: {} Left: {} Right: {})".format(self.value,self.left,self.right)

def find_subtree(s, t):
  if not s:
    return True

  if not t:
    return False

  if helper(s,t):
    return True
  return find_subtree(s, t.left) or find_subtree(s,t.right)

def helper(root, subroot):
  if not root and not subroot:
    return True

  if root and subroot and root.value == subroot.value:
    return helper(root.left, subroot.left) and helper(root.right, subroot.right) 


  

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

#print(find_subtree(s, t))
# True
