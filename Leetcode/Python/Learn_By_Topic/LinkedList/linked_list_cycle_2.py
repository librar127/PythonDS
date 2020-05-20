# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow = head
        fast = head
        
        while fast:
            fast = fast.next
            slow = slow.next
            
            if fast:
                fast = fast.next
            else:
                return None
            
            if slow == fast:
                slow = head
                index = 0
                while slow and fast:
                    if slow == fast:
                        #output = "tail connects to node index {}".format(index)
                        #print(output)
                        return slow
                    slow = slow.next
                    fast = fast.next
                    index += 1
                
        return None
        
