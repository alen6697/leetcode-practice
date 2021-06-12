# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = set() # create a set to store th recovered tree then it will take O(1) to search
        self.createTree(root, 0)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.tree
        
    def createTree(self, root, x):
        if root == None:
            return None
        
        self.tree.add(x)
        if root.left != None:
            self.createTree(root.left, 2 * x + 1)
        
        if root.right != None:
            self.createTree(root.right, 2 * x + 2)
