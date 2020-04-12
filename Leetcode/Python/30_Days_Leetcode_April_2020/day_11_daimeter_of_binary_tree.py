
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def buildTree(self, root, curr_index, nums):
        if curr_index < len(nums):
            root = TreeNode(nums[curr_index])
            
            root.left = self.buildTree(root.left, 2*curr_index+1, nums)
            root.right = self.buildTree(root.right, 2*curr_index+2, nums)
            
        return root
    
    def inOrderTraversal(self, root):
        ## Level Order Traversal
        
        if not root:
            return
        self.inOrderTraversal(root.left)
        print(root.val)
        self.inOrderTraversal(root.right)
    
    def preOrderTraversal(self, root):
        ## Level Order Traversal
        
        if not root:
            return
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)
    
    def postOrderTraversal(self, root):
        ## Level Order Traversal
        
        if not root:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.val)
            
            
    def heightOfBinaryTree(self, root):
        if not root:
            return 0
        
        left_height = 1+self.heightOfBinaryTree(root.left)   
        right_height = 1+self.heightOfBinaryTree(root.right)   
        
        return max(left_height, right_height)
    
    def diameterOfBinaryTree(self, root):
        
        if not root:
            return 0
        
        # Check the diameter of the current node
        node_diameter = self.heightOfBinaryTree(root.left)+ self.heightOfBinaryTree(root.right) 
        
        # check the diameter of the left node stored already
        left_diameter = self.diameterOfBinaryTree(root.left)
         # check the diameter of the right node stored already
        right_diameter = self.diameterOfBinaryTree(root.right)
        

        return max(node_diameter, max(left_diameter, right_diameter))
        
nums = [1, 2, 3, 4, 5]
btree = BinaryTree()
root = btree.buildTree(None, 0, nums)
btree.inOrderTraversal(root)
print()
btree.preOrderTraversal(root)
print()
btree.postOrderTraversal(root)

print(btree.diameterOfBinaryTree(root))

print()
print("Hieght: ", btree.heightOfBinaryTree(root))

print()
print("Diameter: ", btree.diameterOfBinaryTree(root))