class Solution:
    
    # Bottom-Up Recursion    
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_depth = 1+self.maxDepth(root.left)
        right_depth = 1+self.maxDepth(root.right)
        
        return max(left_depth, right_depth)