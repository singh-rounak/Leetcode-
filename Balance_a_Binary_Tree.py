# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        
        nums = []
        
        def inorder( node,nums):
            '''
            Convert BST to ascending sequence
            '''    
            if node:
                
                inorder( node.left, nums )
                nums.append( node.val )
                inorder( node.right, nums )
                
        # ----------------------------------------
        
        def sequence_to_balanced_BST( left, right, nums):
            '''
            Convert ascending sequence to balanced BST
            '''
            if left > right:
                # Base case:
                return None
            
            else:
                # General case:

                mid = left + ( right - left ) // 2

                root = TreeNode( nums[mid] )

                root.left = sequence_to_balanced_BST( left, mid-1, nums)
                root.right = sequence_to_balanced_BST( mid+1, right, nums)

                return root
        
        # ----------------------------------------
		
        # Flatten original BST into a ascending sorted sequence.
        inorder( root, nums )
        
		# Convert asecnding sorted sequence into Balanced BST by the algorithm in Leetcode #108
        return sequence_to_balanced_BST( left = 0, right = len(nums)-1, nums = nums)