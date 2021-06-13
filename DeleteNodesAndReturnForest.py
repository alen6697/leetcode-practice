# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        forest = [root]
        for deleteNode in to_delete:
            tmpForest = []
            for r in forest:
                if r.val != deleteNode:
                    tmpForest.append(r)
                else:
                    if r.left != None:
                        tmpForest.append(r.left)
                    if r.right != None:
                        tmpForest.append(r.right)
                self.deleteNode(r, deleteNode, tmpForest)
                
            forest = list(tmpForest)
        
        return forest
    
    def deleteNode(self, root, deleteNode, forest):
        if root == None:
            return
        
        if root.left != None:
            if root.left.val == deleteNode:
                if root.left.left != None:
                    forest.append(root.left.left)
                if root.left.right != None:
                    forest.append(root.left.right)
                root.left = None
            else:
                self.deleteNode(root.left, deleteNode, forest)
                
        if root.right != None:
            if root.right.val == deleteNode:
                if root.right.left != None:
                    forest.append(root.right.left)
                if root.right.right != None:
                    forest.append(root.right.right)
                root.right = None
            else:
                self.deleteNode(root.right, deleteNode, forest)
                
