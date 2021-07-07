# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        we recurrsively traverse tree and put root.val to dict with level as key
        right most is the last one to be put to dict
        so we can get last one to output from each key
        """
        levelMap = collections.defaultdict(list)
        self.viewRightSide(root, 1, levelMap)
        
        output = []
        for key in sorted(levelMap.keys()):
            output.append(levelMap[key][-1])
            
        return output
    
    def viewRightSide(self, root, level, levelMap):
        if root == None:
            return
        
        levelMap[level].append(root.val)
        self.viewRightSide(root.left, level + 1, levelMap)
        self.viewRightSide(root.right, level + 1, levelMap)
