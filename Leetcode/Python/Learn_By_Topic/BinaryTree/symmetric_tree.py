# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive using Level Order
    def compare(self, left, right):
        if left is None and right is None:
            return True
        
        elif left and right:
            return (left.val == right.val) and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        
        return False        
        
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.compare(root.left, root.right)
        
        
    # Iterative using Level Order
    def isSymmetric_Iterative(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        queue_1 = [root]
        queue_1.insert(0, None)
        
        queue_2 = [root]
        queue_2.insert(0, None)
        
        nodes_at_level_1 = []
        nodes_at_level_2 = []
        
        while queue_1 and queue_2:
            
            root_1 = queue_1.pop()
            root_2 = queue_2.pop()
            
            if root_1 and root_2:
            
                if root_1.left:
                    queue_1.insert(0, root_1.left)
                    nodes_at_level_1.append(root_1.left.val)
                else:                    
                    nodes_at_level_1.append(-1)
                
                if root_1.right:
                    queue_1.insert(0, root_1.right)
                    nodes_at_level_1.append(root_1.right.val)
                else:                    
                    nodes_at_level_1.append(-1)
                    
                
                if root_2.right:
                    queue_2.insert(0, root_2.right)
                    nodes_at_level_2.append(root_2.right.val)
                else:                    
                    nodes_at_level_2.append(-1)
                
                if root_2.left:
                    queue_2.insert(0, root_2.left)
                    nodes_at_level_2.append(root_2.left.val)
                else:                    
                    nodes_at_level_2.append(-1)
                    
            else:
                print(nodes_at_level_1, nodes_at_level_2)
                if not nodes_at_level_1 == nodes_at_level_2:
                    return False
                
                nodes_at_level_1 = []
                nodes_at_level_2 = []
                if queue_1 and queue_2:
                    queue_1.insert(0, None)                    
                    queue_2.insert(0, None)
                
        return True