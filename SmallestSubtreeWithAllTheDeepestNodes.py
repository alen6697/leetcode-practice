# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.max = -1
        self.node = None
        self.dfs(root, 0)
        
        return self.node
    
    def dfs(self, root, depth):
        if root == None:
            return depth - 1
        
        leftDepth = self.dfs(root.left, depth + 1)
        rightDepth = self.dfs(root.right, depth + 1)
        self.max = max(self.max, depth)
        
        if leftDepth == self.max and rightDepth == self.max:
            self.node = root
            
        return max(leftDepth, rightDepth)
