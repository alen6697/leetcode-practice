# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        
        self.insertNode(root, val)
        
        return root
    
    def insertNode(self, root, val):
        if root is None:
            return 
        
        if val < root.val:
            if root.left == None:
                node = TreeNode(val)
                root.left = node
            else:
                self.insertNode(root.left, val)
        else:
            if root.right == None:
                node = TreeNode(val)
                root.right = node
            else:
                self.insertNode(root.right, val)
