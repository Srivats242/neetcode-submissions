# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Correct Solution
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # My Solution
        #root_values = []
        #root_length = 0
        #i = 0
        #for i in root:
            #if ((root == 0) || (root == 1) || (root = 2) || (root = 3) || (root == 4) || (root = 5) || (root = 6) || (root == 7) || (root = 8) || (root == 9) || (root = 10)):
               # i += 1
               # root_length += 1
           # else:
              #  return 0
        #return root_length

        

