# Jacob Stephens / January 31, 2025
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # to be the same tree, 2 conditions must be met
        # 1. values of root are the same
        # 2. both subtrees are the same
        def checkSameTree(root1, root2):

            if (not root1 and root2) or (root1 and not root2):
                return False
            if not root1 and not root2:
                return True 

            return checkSameTree(root1.left, root2.left) and checkSameTree(root1.right, root2.right) and root1.val == root2.val

        def dfs(root):
            
            # if end of dfs, return False for that node
            if not root:
                return False
            
            # if any nodes are same as subroot, return True
            if checkSameTree(root, subRoot):
                return True

            # return True if one True exists
            return dfs(root.left) or dfs(root.right)


        return dfs(root) 

