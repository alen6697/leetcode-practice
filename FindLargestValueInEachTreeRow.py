# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.levelMax = collections.defaultdict(lambda:-2**31) # initialize to keep max number of each level
        self.traverseTree(root, 1)
        
        result = []
        keys = self.levelMax.keys()
        keys.sort()
        for key in keys:
            result.append(self.levelMax[key])
        
        return result
        
    def traverseTree(self, root, level):
        if root == None:
            return
        
        self.levelMax[level] = max(self.levelMax[level], root.val)
        self.traverseTree(root.left, level + 1)
        self.traverseTree(root.right, level + 1)
