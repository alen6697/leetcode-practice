"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        output = []
        levelDist = collections.defaultdict(list)
        self.traverseTree(root, 0, levelDist)
        
        keys = levelDist.keys()
        keys.sort()
        for key in keys:
            output.append(levelDist[key])
                          
        return output
                          
    def traverseTree(self, root, depth, levelDist):
        if root == None:
            return
        
        levelDist[depth].append(root.val)
        for child in root.children:
            self.traverseTree(child, depth + 1, levelDist)
