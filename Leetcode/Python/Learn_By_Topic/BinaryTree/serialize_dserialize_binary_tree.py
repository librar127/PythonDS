# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def s_helper(self, root, string):
        if root is None:
            string += 'None,'        
        else: 
            string += str(root.val)+','
            string = self.s_helper(root.left, string)
            string = self.s_helper(root.right, string)
            
        return string

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.s_helper(root, '')
        

    def d_helper(self, data):
        
        if data[0] == 'None':
            data.pop(0)
            return None
        else:
            root = TreeNode(data.pop(0))
            root.left = self.d_helper(data)
            root.right = self.d_helper(data)
            
        return root
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        node_list = data[0:len(data)-1].split(',')
        root = self.d_helper(node_list)
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))