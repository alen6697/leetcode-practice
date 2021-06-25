class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if len(nums) == 0:
            return res
        
        res[0] = self.findFirst(nums, target)
        res[1] = self.findLast(nums, target)
                        
        return res
    
    def findFirst(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:  # find leftmost so try to reach left part
                right = mid
            else:
                left = mid
                
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
        
    def findLast(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target: # find rightmost so try to reach right part
                left = mid
            else:
                right = mid
                
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
