# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    
    # Tn = O(N), Sn = O(1)
    def connect(self, root):
        
        if not root:
            return
        
        leftmost = root
        
        while leftmost.left:
            
            
            head = leftmost            
            while head:
                
                # 1
                head.left.next = head.right
                
                # 2
                if head.next:
                    head.right.next = head.next.left
                    
                head = head.next
                
            leftmost = leftmost.left
            
        return root
    
    # Tn = O(N), Sn = O(N)
    def connect_2(self, root):
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