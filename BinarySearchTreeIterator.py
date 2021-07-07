# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.output = []
        self._inorder(root)
        self.point = -1

    def next(self):
        """
        :rtype: int
        """
        self.point = self.point + 1
        
        return self.output[self.point]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.point + 1 < len(self.output):
            return True
        else:
            return False
        
    def _inorder(self, root):
        if root == None:
            return
        
        self._inorder(root.left)
        self.output.append(root.val)
        self._inorder(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
