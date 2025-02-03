# Jacob Stephens - February 1, 2025
# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = collections.deque([(root, 0)])
        res = []
        prevLevel = 0
        prevNode = None
        while queue:
            node, level = queue.pop()

            # if change in level, add last seen node
            if prevLevel != level:
                res.append(prevNode.val)
            
            for neighbor in [node.left, node.right]:
                if neighbor:
                    queue.appendleft((neighbor, level + 1))

            # remember previous node and level
            prevLevel = level
            prevNode = node

        res.append(node.val)
        return res

