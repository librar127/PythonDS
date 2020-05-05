# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left, right, inorder, preorder):
        
        if left > right:
            return None
        
        val = preorder.pop(0)
        index = inorder.index(val)
        
        root = TreeNode(val, None, None)
        root.left = self.helper(left, index-1, inorder, preorder)
        root.right = self.helper(index+1, right, inorder, preorder)
        
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        n = len(preorder)-1
        return self.helper(0, n, inorder, preorder)
        