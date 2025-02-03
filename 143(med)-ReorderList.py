# Jacob Stephens - January 21, 2025
# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # get length and midpt of list
        c = head
        length = 0
        while c != None:
            c = c.next
            length += 1
        
        if length == 1:
            return

        m = length // 2 
        print(f'{m=}')

        # split list into 2 lists
        c = head
        i = 0
        l2_head = None
        while c != None:

            if i == m - 1:
                l2_head = c.next
                c.next = None
                
            c = c.next
            i += 1
        
        print(f'{l2_head.val=}')

        # reverse second list
        p = None
        c = l2_head
        while c != None:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        l2_head = p
        
        # merge lists
        l = head
        r = l2_head
        while l != None:
            tmpr = r.next
            tmpl = l.next
            l.next = r

            if tmpl == None and tmpr != None:
                return
            else:
                r.next = tmpl
            
            l = tmpl
            r = tmpr


        # print list
        c = head
        while c != None:
            print(c.val)
            c = c.next
        