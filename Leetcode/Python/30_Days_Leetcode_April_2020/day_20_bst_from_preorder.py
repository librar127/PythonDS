# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructBST(self, preorder):
        
        if not preorder:
            return None
        
        node = TreeNode(preorder.pop(0))
        middle = len(preorder)
        
        for index, each in enumerate(preorder):
            if each > node.val:
                middle = index
                break
            
        node.left = self.constructBST(preorder[:middle])
        node.right = self.constructBST(preorder[middle:])
        
        return node
        
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        return self.constructBST(preorder)
            
        
        