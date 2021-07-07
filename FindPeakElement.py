class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums)
        
        return nums.index(_max)
