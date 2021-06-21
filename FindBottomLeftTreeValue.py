# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # idea is we keep appending node to queue then take out from queue according to order right node then left node
        # last one is leftmost node
        """
           2
         /   \
       1       3

       2  <- fisrt
       3  1 <- second
        """
        
        queue = []
        queue.append(root)
        
        while queue:
            root = queue.pop(0)
            if root.right != None:
                queue.append(root.right)
                
            if root.left != None:
                queue.append(root.left)

        return root.val
