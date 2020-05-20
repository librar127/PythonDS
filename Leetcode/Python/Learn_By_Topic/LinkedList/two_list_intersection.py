# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def processList(self, diff_count, headA, headB):
        count = 0
        while count < diff_count:
            print(count, diff_count)
            headA = headA.next
            count += 1
        
        
        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next            
            headB = headB.next
            
        return None
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        len_A = 0
        len_B = 0
        
        A = headA
        B = headB
        
        while headA:
            headA = headA.next
            len_A += 1
        
        while headB:
            headB = headB.next
            len_B += 1
        
        diff = abs(len_A-len_B)
        if len_A > len_B:
            return self.processList(diff, A, B)
        else:
            print('B', diff)
            return self.processList(diff, B, A)
            
        
        