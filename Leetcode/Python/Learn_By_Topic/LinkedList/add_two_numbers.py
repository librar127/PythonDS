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
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        head = current = None
        while l1 and l2:
            val = l1.val + l2.val + carry
            print("VAL: ", val)
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            
            node = ListNode(val)
            
            if current == None:
                current = node
                head = current
            else:
                current.next = node
                current = current.next
                
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            val = l1.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            
            node = ListNode(val)
            current.next = node
            current = current.next
            l1 = l1.next
            
        while l2:
            val = l2.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            
            node = ListNode(val)
            current.next = node
            current = current.next
            l2 = l2.next
            
        if carry > 0:
            node = ListNode(carry)
            current.next = node
            current = current.next
            
            
        return head