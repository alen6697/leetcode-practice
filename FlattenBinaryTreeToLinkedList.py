# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        """
        1. connect root.right to leftmost
        2. replace root.right with root.left
        3. root.left is assigned to None
        4. return rightmost if rightmost is not none otherwise return leftmost if leftmost is not none otherwise root
        """
        self.traverse(root)
               
    def traverse(self, root):
        if root == None:
            return None
        
        leftMost = self.traverse(root.left)
        rightMost = self.traverse(root.right)
        
        if leftMost != None:
            leftMost.right = root.right
            root.right = root.left
            root.left = None
            
        if rightMost: return rightMost
        if leftMost: return leftMost
        
        return root
