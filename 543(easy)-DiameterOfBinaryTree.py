# Jacob Stephens - January 25, 2025
# https://leetcode.com/problems/diameter-of-binary-tree/description/

#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiameter = 0
        def dfs(root):
            nonlocal maxDiameter

            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            diameter = leftHeight + rightHeight
            maxDiameter = max(maxDiameter, diameter)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return maxDiameter
