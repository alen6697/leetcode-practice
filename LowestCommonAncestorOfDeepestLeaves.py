# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.node = None
        self.maxDepth = -1
        self.dfs(root, 0)    
        
        return self.node
        
        
    def dfs(self, root, depth):
        if root == None:
            return depth - 1
        
        leftDepth = self.dfs(root.left, depth + 1)
        rightDepth = self.dfs(root.right, depth + 1)
        
        if depth > self.maxDepth:
            self.maxDepth = depth
            
        if leftDepth == self.maxDepth and rightDepth == self.maxDepth:
            self.node = root
        
        return max(leftDepth, rightDepth)
