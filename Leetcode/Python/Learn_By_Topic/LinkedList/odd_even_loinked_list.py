# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        even_head = None
        current = head
        even = None
        even_flag = True
        
        odd_head = current
        odd = odd_head
        
        while current.next:
            if even_flag:
                even_flag = False
                if not even_head:
                    even_head = odd_head.next
                    even = even_head
                else:
                    even_head.next = odd_head.next
                    even_head = even_head.next
            else:
                even_flag = True
                odd_head.next = even_head.next
                odd_head = odd_head.next
                    
            current = current.next
        
        if even_head:
            even_head.next = None
        odd_head.next = even
        return odd