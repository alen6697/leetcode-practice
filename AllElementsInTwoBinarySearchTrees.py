# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res = []
        
        self.traverseTree(root1, res)
        self.traverseTree(root2, res)
        
        res.sort()
        
        return res
    
    def traverseTree(self, root, tree):
        if root == None:
            return
        
        self.traverseTree(root.left, tree)
        tree.append(root.val)
        self.traverseTree(root.right, tree)
