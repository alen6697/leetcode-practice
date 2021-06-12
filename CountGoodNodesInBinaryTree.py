# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 1
        self.traverseTree(root, root.val, None)
        
        return self.count
    
    def traverseTree(self, root, maximum, parent):
        if root == None:
            return
        
        if parent != None:
            if maximum <= root.val:
                self.count = self.count + 1
            maximum = max(maximum, root.val)
            
        if root.left != None:
            self.traverseTree(root.left, maximum, root)
            
        if root.right != None:
            self.traverseTree(root.right, maximum, root)
