# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.createTree(preorder, 0, len(preorder))
    
    def createTree(self, preorder, start, end):
        if start >= end:
            return None
        
        root = TreeNode(preorder[start])
        nextStart = start + 1
        while nextStart < end and preorder[nextStart] < preorder[start]:
            nextStart = nextStart + 1
            
        root.left = self.createTree(preorder, start + 1, nextStart)
        root.right = self.createTree(preorder, nextStart, end)
        
        return root
