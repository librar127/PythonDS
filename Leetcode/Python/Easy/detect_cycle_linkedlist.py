# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    ### Method 1 - Using Slow and Fast Pointers
    def hasCycle(self, head):
        slow = head
        fast = head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:           
                return True
        return False
        
    ### Method 2 - Using Hashmap
    def hasCycle_Hashmap(self, head):
        if head is None:
            return False
        
        hashset = {}
        while head is not None:
            if head in hashset.keys() and head.next == hashset[head]:
                return True
            else:
                hashset[head] = head.next
            head = head.next
        return False
        
