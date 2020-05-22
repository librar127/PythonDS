# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        new_head = Node(0, None, head, None)
        prev = new_head
        
        stack = []
        stack.append(head)
        
        while stack:
            
            node = stack.pop()
            node.prev = prev
            prev.next = node
            
            if node.next:    
                stack.append(node.next)
                
            if node.child:
                stack.append(node.child)
                node.child = None
            
            prev = node    
        
        head = new_head
        new_head = new_head.next
        head = None
        new_head.prev = head
        return new_head
    