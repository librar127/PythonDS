# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def reverseList(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
            
        return prev
        
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next: 
            return head
        
        current  = head
        
        # find the length of the list
        n = 0
        while current:
            current = current.next
            n += 1
        
        # if k is > length of the list
        if k >= n:
            k = k%n
        
        if k == 0:
            return head
            
        # find the kth node
        print("K: ", k)
        first_pointer = head
        next_pointer = head
        count = 0
        while count < k:
            next_pointer = next_pointer.next
            count += 1
        
        while next_pointer.next:
            next_pointer = next_pointer.next
            first_pointer = first_pointer.next            
        
        new_head = first_pointer.next
        current = new_head
        first_pointer.next = None
        
        while current.next:
            current = current.next
        current.next = head
        
        return new_head