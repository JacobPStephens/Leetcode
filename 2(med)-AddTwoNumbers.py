# Jacob Stephens - January 25, 2025
# https://leetcode.com/problems/add-two-numbers/description/
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getLength(head):
            l = 0
            c = head
            while c:    
                l += 1
                c = c.next
            return l

        def addLeadingZeros(head, n):
            c = head
            while c.next:
                c = c.next
            for _ in range(n):
                new = ListNode(0, None)
                c.next = new
                c = c.next

        def printList(head):
            c = head
            while c:
                print(c.val, end= " ")
                c = c.next
            print()

        c1_length = getLength(l1)
        c2_length = getLength(l2)

        diff = c1_length - c2_length
        if diff > 0:
            addLeadingZeros(l2, diff)
        else:
            addLeadingZeros(l1, -1 * diff)

        c1 = l1
        c2 = l2
        c3 = None
        carry = 0
        while c1 and c2:
        
            p3 = c3
            digit = (c1.val + c2.val) % 10
            
            if digit + carry == 10:
                c3 = ListNode(0, None)
                carry = 1
            else:
                c3 = ListNode(digit + carry, None)
                carry = (c1.val + c2.val) // 10

            # if first node, get reference to head
            # otherwise update prev
            if not p3:
                l3_head = c3
            else:
                p3.next = c3

            c1 = c1.next
            c2 = c2.next

        if carry:
            c3.next = ListNode(1, None)

        return l3_head


