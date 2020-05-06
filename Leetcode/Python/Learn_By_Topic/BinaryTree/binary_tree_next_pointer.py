# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return 
        
        queue = [root]
        
        while queue:
            
            node = queue.pop(0)
            
            if node.left and node.right:
                    
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                    
                queue.append(node.left)
                queue.append(node.right)
        
        return root
                
                
            
            
            
            
            
            
