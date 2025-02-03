# Jacob Stephens - February 2, 2025
# https://leetcode.com/problems/validate-binary-search-tree/description/

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, floor, ceiling):

            if not root:
                return True

            inRange = (floor < root.val < ceiling)
            
            leftBST = dfs(root.left, floor, root.val)
            rightBST = dfs(root.right, root.val, ceiling)
            
            return inRange and leftBST and rightBST
            
        return dfs(root, -float('inf'), float('inf'))
