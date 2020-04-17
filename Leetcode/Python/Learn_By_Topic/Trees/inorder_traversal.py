# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, result):
        if not root:
            return 
        
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
        
    def inorderTraversal_recursive(self, root):
        result = []
        
        self.traverse(root, result)
        return result
    
    def inorderTraversal(self, root):
        
        if not root:
            return []
        
        result = []
        stack = []
        
        while True:
            
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return result

            
            node = stack.pop()
            result.append(node.val)
            root = node.right