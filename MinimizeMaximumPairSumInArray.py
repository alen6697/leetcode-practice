class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        nums.sort()
        for i in range(len(nums)):
            maximum = max(maximum, nums[i] + nums[len(nums) - i - 1])
            
        return maximum
