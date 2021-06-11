# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createTree(nums)
        
    def createTree(self, nums):
        if len(nums) == 0:
            return None
        else:
            maximum = max(nums)
            idx = nums.index(maximum)
            r = TreeNode()
            r.val = maximum
            r.left = self.createTree(nums[:idx])
            r.right = self.createTree(nums[idx+1:])
            
            return r
