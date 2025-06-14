# Jacob Stephens - January 23, 2025
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        p = None
        c = head
        a = head
        for _ in range(n):
            a = a.next

        while a != None:
            p = c
            c = c.next
            a = a.next
        
        if not p:
            return c.next

        p.next = c.next
        return head
        