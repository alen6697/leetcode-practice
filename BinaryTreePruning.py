# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.deleteNode(root)
        
        if root.val == 0 and root.left == None and root.right == None:
            return None
        
        return root
    
    def deleteNode(self, root):
        if root == None:
            return
        
        if root.left != None:
            self.deleteNode(root.left)
            if root.left.val == 0 and root.left.left == None and root.left.right == None:
                root.left = None
                
        if root.right != None:
            self.deleteNode(root.right)
            if root.right.val == 0 and root.right.left == None and root.right.right == None:
                root.right = None
