class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums, 0, len(nums)-1)
        
        return nums
        
    def quickSort(self, nums, start, end):
        if start >= end:
            return
        
        pivot = nums[start + (end - start) // 2]
        left = start
        right = end
        while left < right:
            while left <= right and nums[left] < pivot:
                left = left + 1
                
            while left <= right and nums[right] > pivot:
                right = right - 1
                
            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left = left + 1
                right = right - 1
                
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
