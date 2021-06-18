class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        output = 0
        count = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count = count + 1
            else:
                output = max(output, count)
                count = 1
                    
        output = max(output, count)   
        return output
