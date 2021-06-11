# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Store result to return in res
        self.res = 0
        
        #Iterate over the tree using DFS
        self.dfs(root, "")
        
        #Return res
        return self.res
    
    def dfs(self, node, curr):
        
        #If node.left and node.right are None, we have reached the leaf node
        #We update res with the interger value of the binary string
        if not node.left and not node.right: 
            self.res = self.res + int(curr + str(node.val), 2)
        
        #Traverse recursively for DFS
        if node.left:
            self.dfs(node.left, curr + str(node.val))
        if node.right:
            self.dfs(node.right, curr + str(node.val))
