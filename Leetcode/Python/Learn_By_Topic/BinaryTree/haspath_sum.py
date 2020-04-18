# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum_Recursion(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and sum == root.val:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        stack = []
        
        while True:            
                
            while root:
                sum = sum - root.val
                stack.append((root, sum))
                root = root.left
            
            if not stack:
                return False
            
            
            (node, sum) = stack.pop()                
            if node and not node.left and not node.right and sum == 0:
                return True
            root = node.right
            
        return False