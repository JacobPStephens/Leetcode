# Jacob Stephens - January 24, 2025
# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
        toCopy = dict()

        # go through first list and create a copy of each node
        c = head
        while c:
            tmp = Node(c.val, None, None)
            toCopy[c] = tmp

            c = c.next

        for item in toCopy.items():
            node = item[0]
            copyNode = item[1]

            if node.next:
                copyNode.next = toCopy[node.next]

            if node.random:
                copyNode.random = toCopy[node.random]

        return toCopy[head]


