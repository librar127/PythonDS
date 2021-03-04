# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        summ = 0
        if not root:
            return 0
        
        elif root.val >= low and root.val<=high:
            summ += root.val
            
        return summ + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        