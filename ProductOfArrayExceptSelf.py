class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        nums    1, 2, 3, 4
        
        answer  1, 1, 2, 6  <-- first loop
        
        answer  24, 12, 8, 6  <-- right = right * nums[i] then answer[i] = answer[i] * right
        """
        answer = [1] * len(nums)
        for i in range(1, len(nums)):  # scan from left to right
            answer[i] = answer[i - 1] * nums[i - 1]  # first loop we store left product in answer
            
        right = nums[-1]    
        for i in range(len(nums) - 2, -1, -1): # scan from right to left
            answer[i] = answer[i] * right
            right = right * nums[i]    # we want to store right product in right
            
        return answer
