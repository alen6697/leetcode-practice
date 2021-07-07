# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.traverseTree(root, "")
        
        return self.sum
    
    def traverseTree(self, root, res):
        if root == None:  # if node is none, we don't have to do anything
            return
        
        if root.left == None and root.right == None: # if all children are None, mean it is leaf. then we need to add to sum
            res = res + str(root.val)
            self.sum = self.sum + int(res)
            return
        
        res = res + str(root.val)
        self.traverseTree(root.left, res)
        self.traverseTree(root.right, res)
