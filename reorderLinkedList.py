#Definition for singly-linked list.

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def getHead(self):
        return self.head
    
    def printList(self):
        c = self.head
        tries = 0
        while c != None and tries < 20:
            print("VAL:", c.getVal())
            c = c.getNext()
            tries += 1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next
    
    def setVal(self, val):
        self.val = val

    def setNext(self, next):
        self.next = next


def main(): 
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    n7 = ListNode(7, None)
    n6 = ListNode(6, n7)
    n5 = ListNode(5, n6)
    n4 = ListNode(4, n5)
    
    left_list = LinkedList(n1)
    right_list = LinkedList(n4)

    #reverse(left_list.getHead())
    merge(left_list.getHead(), right_list.getHead())
    # print(left_list.getHead().getVal())
    left_list.printList()

def merge(head1, head2):

    l = head1
    r = head2
    
    #print(type(r))
    #print(l.getVal(), r.getVal())
    while l != None:
        if l != None:
            print("L:",l.getVal())
        else:
            print("l = None")
        if r != None:
            print("R:", r.getVal())
        else:
            print("r = None")
        tmpr = r.getNext()
        tmpl = l.getNext()
        l.setNext(r)

        if tmpl == None and tmpr != None:
            return
        else:
            r.setNext(tmpl)

        #if tmpl == None and tmpr != None:
        l = tmpl
        r = tmpr


def reverse(head1):
    
    p = None
    c = head1
    while c != None:
        if p != None:
            print(f"{p.getVal()=}")
        else:
            print("p = None")
        print(f"{c.getVal()=}")
        print()
        
        tmp = c.getNext()
        c.setNext(p)
        p = c
        c = tmp

main()