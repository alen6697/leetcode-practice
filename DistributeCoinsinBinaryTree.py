# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.balance(root)
        
        return self.ans
    
    def balance(self, root):
        if root == None:
            return 0
        
        left = self.balance(root.left)  # each balance of node is node.val - 1
        right = self.balance(root.right)
        
        # abs(left) means how many moves happen in left tree
        self.ans = self.ans + abs(left) + abs(right)
        
        return root.val - 1 + left + right # root's balance is root.val - 1 + balance(left) + balance(right)
