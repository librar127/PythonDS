"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # Copied Solution
    def connect_(self, root):
        if not root:
            return
        queue = []
        
        queue.append(root)        
        tail = root
        
        while queue:
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if node == tail:
                node.next = None
                tail = queue[-1] if len(queue) > 0 else None
            else:
                node.next = queue[0]
                
        return root

    def connect(self, root)':
        
        queue = [root]
        level_break = Node('NB', None, None, None)
        queue.append(level_break)
        prev = None
        
        while queue:
            
            node = queue.pop(0)
            
            if node and node.val != 'NB':
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                if prev:
                    prev.next = node
            else:
                if not queue:
                    return root
                if node and node.val == 'NB':
                    level_break = Node('NB', None, None, None)
                    queue.append(level_break)
                    
            prev = node
            
        return root