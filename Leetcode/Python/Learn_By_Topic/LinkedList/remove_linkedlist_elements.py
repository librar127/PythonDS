# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head:
            return head
        
        while head and head.val == val:
            node = head
            head = head.next
        
        current = head
        while current:
            
            if current.next and current.next.val == val:
                current.next = current.next.next  
            else:
                current = current.next  
                
        return head  