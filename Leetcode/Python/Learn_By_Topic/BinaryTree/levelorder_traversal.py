# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        queue.insert(0, None)
        
        result = []
        level_result = []
        
        while queue:
            
            root = queue.pop()
            if root:
                level_result.insert(0, root.val)

                if root.left:
                    queue.insert(0, root.left)
                if root.right:
                    queue.insert(0, root.right)
                
            else:   
                result.append(level_result[::-1])
                level_result = []
                if queue:
                    queue.insert(0, None)
                
        return result
        