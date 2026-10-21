# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        treeNodeList = []
        treeNodeLength = 0
        for i in range(len(treeNodeList)):
            treeNodeList.append([TreeNode])
            treeNodeLength += 1
            if len(treeNodeList) < 1:
                return 0
            else: 
                return len(treeNodeList)
        return len(treeNodeList)    


