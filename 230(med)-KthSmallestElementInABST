# Jacob Stephens - February 2, 2025
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        i = 0
        res = None
        def inOrder(root):
            nonlocal i, res
            if not root or i >= k:
                return
            
            inOrder(root.left)
            
            i += 1
            print(f'{root.val=} {i=}')

            if i == k:
                res = root.val
                return

            inOrder(root.right)

        inOrder(root)

        return res
        