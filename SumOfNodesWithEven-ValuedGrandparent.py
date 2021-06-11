# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, None, None)
        
    def dfs(self, root, parent, grandparent):
        res = 0
        if root == None:
            return res
        
        if grandparent is not None and grandparent.val % 2 == 0:
            res = res + root.val
            
        return res + self.dfs(root.left, root, parent) + self.dfs(root.right, root, parent)
