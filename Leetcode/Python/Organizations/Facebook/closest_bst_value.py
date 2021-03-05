# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        queue = [root]
        result = root.val
        min_diff = abs(root.val - target)
        
        while queue:
            
            current = queue.pop()            
            diff = abs(current.val - target)
            if diff < min_diff:
                min_diff = diff
                result = current.val
                
            if current.left:
                queue.insert(0, current.left)
                
            if current.right:
                queue.insert(0, current.right)
                
        return result
            