"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        levelMap = collections.defaultdict(list)
        self.traverse(root, 1, levelMap)
        
        for k, v in levelMap.items():
            for i in range(len(v) - 1):
                v[i].next = v[i+1]
                
        return root
        
    def traverse(self, root, level, levelMap):
        if root == None:
            return root
        
        levelMap[level].append(root)
        self.traverse(root.left, level + 1, levelMap)
        self.traverse(root.right, level + 1, levelMap)
