# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        self.deleteNode(root, target)
        
        if root.val == target and root.left == None and root.right == None:
            return None
        
        return root
    
    def deleteNode(self, root, target):
        if root == None:
            return
        
        if root.left != None:
            self.deleteNode(root.left, target)
            if root.left.val == target and root.left.left == None and root.left.right == None:
                root.left = None
        
        if root.right != None:
            self.deleteNode(root.right, target)
            if root.right.val == target and root.right.left == None and root.right.right == None:
                root.right = None
