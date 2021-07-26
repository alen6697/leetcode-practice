class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closetSum = sys.maxint
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[left] + nums[right] + nums[i]
                if abs(target - currentSum) < abs(target - closetSum):
                    closetSum = currentSum
                    
                if currentSum <= target:
                    left = left + 1
                else:
                    right = right - 1
                    
        return closetSum
