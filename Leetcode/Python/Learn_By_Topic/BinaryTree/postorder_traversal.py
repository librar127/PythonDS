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
        self.traverse(root.right, result)
        result.append(root.val)

    def postorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        
        result = []

        self.traverse(root, result)
        return result
            

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            
            root = stack.pop()
            result.append(root.val)
            
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
                
        return result[::-1]
            
            
        