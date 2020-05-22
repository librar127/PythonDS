# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

cclass Solution:
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
        
        new_head.next.prev = None
        return new_head.next