# Jacob Stephens - October 19, 2024
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()
        prev, curr = None, head

        while curr != None:

            if curr in visited:
                return True

            visited.add(curr)
            prev = curr
            curr = curr.next
        
        return False
