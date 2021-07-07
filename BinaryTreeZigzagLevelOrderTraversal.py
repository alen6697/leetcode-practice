# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levelMap = collections.defaultdict(list)
        self.traverse(root, 1, levelMap)
        
        keys = sorted(levelMap.keys())
        output = []
        for key in keys:
            if key % 2 == 0:
                output.append(levelMap[key][::-1])
            else:
                output.append(levelMap[key])
                
        return output
        
    def traverse(self, root, level, levelMap):
        if root == None:
            return
        
        levelMap[level].append(root.val)
        self.traverse(root.left, level + 1, levelMap)
        self.traverse(root.right, level + 1, levelMap)
