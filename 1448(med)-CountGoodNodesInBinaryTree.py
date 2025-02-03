# Jacob Stephens - February 2, 2025
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        numGood = 0
        def dfs(root, highest):
            nonlocal numGood

            if not root:
                return

            if root.val >= highest:
                numGood += 1
                highest = root.val

            dfs(root.left, highest)
            dfs(root.right, highest)


        dfs(root, -float('inf'))

        return numGood