# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root == None: # if root is None, just return None
            return None
        
        if root.val < low:  # if root.val is less than low, point root to right child
            return self.trimBST(root.right, low, high)
    
        if root.val > high:
            return self.trimBST(root.left, low, high) # if root.val is greater than high, point root to left child
                
        
        # if root in range, keep trimming left and right chlid tree
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
