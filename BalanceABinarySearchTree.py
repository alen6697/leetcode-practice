# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        treeList = []
        self.covertTree(root, treeList)
        newRoot = self.constructTree(0, len(treeList) - 1, treeList)
        
        return newRoot
    
    def covertTree(self, root, treeList):
        if root == None:
            return
        
        self.covertTree(root.left, treeList)
        treeList.append(root.val)
        self.covertTree(root.right, treeList)
        
    def constructTree(self, start, end, treeList):
        if start > end:
            return None
        
        mid = start + (end - start) // 2
        root = TreeNode(treeList[mid])
        root.left = self.constructTree(start, mid - 1, treeList)
        root.right = self.constructTree(mid + 1, end, treeList)
        
        return root
