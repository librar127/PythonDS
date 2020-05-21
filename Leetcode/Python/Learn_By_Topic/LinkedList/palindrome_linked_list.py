# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        
        current = head
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
    
    def isPalindrome(self, head: ListNode) -> bool: 
        
        if head is None or head.next is None:
            return True
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        
        second = self.reverseList(slow)
        if not fast:
            prev.next = None
        else:            
            prev.next.next = None
            
        
        while second and head:
            if second.val == head.val:
                second = second.next
                head = head.next
            else:
                return False
        
        if second:
            return False
        if head:
            return False
        
        return True