# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        left = self.flipEquiv(root1.left, root2.left)
        right = self.flipEquiv(root1.right, root2.right)
        left2 = self.flipEquiv(root1.left, root2.right)
        right2 = self.flipEquiv(root1.right, root2.left)
        
        return (root1.val == root2.val and left and right) or (root1.val == root2.val and left2 and right2)
