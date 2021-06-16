# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = 0
        self.traverseTree(root, root.val, root.val)
        
        return self.maximum
    
    def traverseTree(self, root, maxValue, minValue):
        tmpMax = max(abs(root.val - maxValue), abs(root.val - minValue))
        self.maximum = max(self.maximum, tmpMax)
        maxValue = max(maxValue, root.val)
        minValue = min(minValue, root.val)
        if root.left:
            # we want maximum difference in a path, so we need to pass max value and min value to next level
            self.traverseTree(root.left, maxValue, minValue)
        if root.right:
            self.traverseTree(root.right, maxValue, minValue)
