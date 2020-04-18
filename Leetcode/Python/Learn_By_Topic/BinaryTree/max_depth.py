# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Bottom-Up Recursion    
    def maxDepth_recursion(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_depth = 1+self.maxDepth(root.left)
        right_depth = 1+self.maxDepth(root.right)
        
        return max(left_depth, right_depth)
    
    # Iterative Approach - Using Queue   
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
                
        queue = [root]
        queue.insert(0, None)
        max_depth = 0
        
        while queue:
            
            root = queue.pop()
            if root:
                if root.left:
                    queue.insert(0, root.left)
                if root.right:
                    queue.insert(0, root.right)
            else:
                max_depth +=1
                if not queue:
                    return max_depth
                else:                
                    queue.insert(0, None)    
                