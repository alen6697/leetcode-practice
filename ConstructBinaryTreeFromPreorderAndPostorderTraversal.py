# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        
        root = TreeNode(post[-1])
        if len(pre) > 1:
            postIndex = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1:postIndex+2], post[:postIndex+1])
            root.right = self.constructFromPrePost(pre[postIndex+2:], post[postIndex+1:-1])
        
        return root
