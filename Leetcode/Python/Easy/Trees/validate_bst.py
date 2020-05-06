# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, root, p_list):
        
        if not root:
            return
        
        self.inorder_traversal(root.left, p_list)
        p_list.append(root.val)
        self.inorder_traversal(root.right, p_list)
        
        return p_list
        
    def isValidBST(self, root):
        
        if not root:
            return True
        
        p_list = self.inorder_traversal(root, [])
        if len(p_list) == len(set(p_list)) and p_list == sorted(p_list):
            return True
        else:
            return False
        