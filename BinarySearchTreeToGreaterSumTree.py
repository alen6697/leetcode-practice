# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.covertTree(root)
        
        return root
        
    def covertTree(self, root):
        if root is not None:
            self.covertTree(root.right)
            self.sum = self.sum + root.val
            root.val = self.sum
            self.covertTree(root.left)
