# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        inorder = []
        self.traverse(root, inorder)

        for i in range(len(inorder) - 1):
            if inorder[i + 1] <= inorder[i]:
                return False
            
        return True
        
    def traverse(self, root, inorder):
        if root == None:
            return
        
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)
