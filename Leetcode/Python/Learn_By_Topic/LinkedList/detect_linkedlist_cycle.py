# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            else:
                return False
            
            if slow == fast:
                return True
            
        return False
        