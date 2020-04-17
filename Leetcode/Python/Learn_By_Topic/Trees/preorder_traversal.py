# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def traverse(self, root, result):
        if root is None:
            return 

        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
            
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        
        result = []
        self.traverse(root, result)
        return result
        
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
            
        result = []
        stack = []        
        stack.append(root)
        
        while len(stack)>0:
            
            node = stack.pop()
            
            
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return result