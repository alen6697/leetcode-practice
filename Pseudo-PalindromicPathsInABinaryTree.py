# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # we are looking for palindromic string
        # in a path, all node happen even time and only one node happen odd times
        self.ans = 0
        cur = [True] * 10
        self.dfs(root, cur)
        
        return self.ans
    
    def dfs(self, root, cur):
        cur[root.val] = not cur[root.val]
        if root.left == None and root.right == None:
            if cur.count(False) <= 1:
                self.ans = self.ans + 1
            
        if root.left:
            self.dfs(root.left, cur)
            
        if root.right:
            self.dfs(root.right, cur)
            
        cur[root.val] = not cur[root.val]
