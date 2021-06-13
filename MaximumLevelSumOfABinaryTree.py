# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        levelSum = collections.defaultdict(int)
        depth = 0
        self.traverseTree(root, 1, levelSum)
        
        maxLevel = 1
        keys = levelSum.keys()
        maximumSum = levelSum[keys[0]]
        for i in range(1, len(keys)):
            if levelSum[keys[i]] > maximumSum:
                maximumSum = levelSum[keys[i]]
                maxLevel = keys[i]
                
        return maxLevel
    
    def traverseTree(self, root, depth, levelSum):
        if root == None:
            return
        
        levelSum[depth] = levelSum[depth] + root.val
        self.traverseTree(root.left, depth + 1, levelSum)
        self.traverseTree(root.right, depth + 1, levelSum)
