# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDepth = self.calculateDepth(root)
        self.res = 0
        self.dfs(root, maxDepth, 0)
        
        return self.res
    
    def calculateDepth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.calculateDepth(root.left), self.calculateDepth(root.right))
        
    def dfs(self, root, maxDepth, depth):
        if root != None:
            if depth + 1 == maxDepth and root.left == None and root.right == None:
                self.res = self.res + root.val
            else:
                self.dfs(root.left, maxDepth, depth + 1)
                self.dfs(root.right, maxDepth, depth + 1)
            
