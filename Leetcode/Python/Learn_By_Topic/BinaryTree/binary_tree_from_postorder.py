# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def helper(self, left, right, inorder, postorder):
        
        if left > right:
            return None
        
        val = postorder.pop()
        root = TreeNode(val, None, None)        
        index = inorder.index(val)
        
        root.right = self.helper(index+1, right, inorder, postorder)
        root.left = self.helper(left, index-1, inorder, postorder)
            
        return root
        
    
    def buildTree(self, inorder, postorder):
        
        n = len(postorder)-1        
        root = self.helper(0, n, inorder, postorder)
        
        return root
        