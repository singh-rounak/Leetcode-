  def find_in_order_successor(self, inputNode):
    self.successor = None

    def helper(node):
        if not node or self.successor:
            return

        helper(node.left)            
        if node.key > inputNode.key and not self.successor:
            self.successor = node
            return
        helper(node.right)


    helper(self.root)
    return self.successor        
        