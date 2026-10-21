# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Neetcode Solution
        result = 0

        # Return the height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal result
            result = max(result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return result
        
        # My Solution
        #treeNodeList = []
        #treeNodeLength = 0
        #for i in range(len(treeNodeList)):
            #treeNodeList.append([TreeNode])
            #treeNodeLength += 1
            #if len(treeNodeList) < 1:
                #return 0
           # else: 
                #return treeNodeLength

        #return len(treeNodeList)    


