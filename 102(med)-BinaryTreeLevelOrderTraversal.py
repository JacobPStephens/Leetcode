# Jacob Stephens - January 30, 2025
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = collections.deque([(root, 0)])
        d = dict()
        
        while queue:
            node, level = queue.pop()

            for child in [node.left, node.right]:
                if child:
                    queue.appendleft((child, level+1))

            # add to dictionary
            if level not in d:
                d[level] = []

            d[level].append(node.val)

        # convert dictionary to nested list
        res = [0] * len(d)
        for l in d.keys():
            res[l] = d[l]

        return res
