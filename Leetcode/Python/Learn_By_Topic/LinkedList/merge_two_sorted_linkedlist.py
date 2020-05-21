# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        current = head = None
        
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
                            
            if head is None:
                head = node
                current = head
            else:
                head.next = node
                head = head.next
        
        while l1:            
            node = ListNode(l1.val)
            if head is None:
                head = node
                current = head
            else:                
                head.next = node
                head = head.next
            l1 = l1.next
            
        while l2:            
            node = ListNode(l2.val)
            if head is None:
                head = node
                current = head
            else:                
                head.next = node
                head = head.next
            l2 = l2.next
        
        #head = self.reverseList(head) 
        return current
        