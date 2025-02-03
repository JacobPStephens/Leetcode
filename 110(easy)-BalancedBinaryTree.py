# Jacob Stephens - January 27, 2025
# https://leetcode.com/problems/balanced-binary-tree/submissions/
# 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def height(root):
            if not root:
                return 0

            return 1 + max(height(root.left), height(root.right))
        
        def is_balanced(root):
            #print(root.val)
            if not root or (not root.left and not root.right):
                return True

            heightDiff = abs(height(root.left) - height(root.right)) <= 1
            childrenBalanced = is_balanced(root.left) and is_balanced(root.right)

            return heightDiff and childrenBalanced

        return is_balanced(root)
