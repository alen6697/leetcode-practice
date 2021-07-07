class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        
        left = 0
        right = len(nums) - 1
        result = nums[0] # assume nums[0] is smallest
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:  # left part is ascending
                result = min(result, nums[left]) # so we get min value then search right part
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1
                
        return result
