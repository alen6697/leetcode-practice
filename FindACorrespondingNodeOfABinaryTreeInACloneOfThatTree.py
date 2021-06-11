# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        self.inorder(original, cloned, target)
        
        return self.res
    
    def inorder(self, original, cloned, target):
        if original is not None:
            self.inorder(original.left, cloned.left, target)
            if original == target:
                self.res = cloned
            self.inorder(original.right, cloned.right, target)
