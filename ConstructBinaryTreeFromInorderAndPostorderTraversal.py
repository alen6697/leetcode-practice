# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(root.val)
        root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
        
        return root
