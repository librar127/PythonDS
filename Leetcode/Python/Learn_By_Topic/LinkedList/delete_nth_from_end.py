# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        A = head
        B = head
        
        length = 0
        while A:
            A = A.next
            length += 1
            
        node_from_start = length-n
        
        if node_from_start == 0:
            head = head.next
            return head
        
        count = 0
        while count < node_from_start-1:
            head = head.next
            count += 1
        
        head.next = head.next.next
        
        return B
        