# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levelMap = collections.defaultdict(list)
        self.traverseTree(root, 1, levelMap)
        
        keys = levelMap.keys()
        keys.sort()
        output = []
        for key in keys:
            output.append(levelMap[key])
            
        return output
        
    def traverseTree(self, root, level, levelMap):
        if root == None:
            return
        
        levelMap[level].append(root.val)
        self.traverseTree(root.left, level + 1, levelMap)
        self.traverseTree(root.right, level + 1, levelMap)
