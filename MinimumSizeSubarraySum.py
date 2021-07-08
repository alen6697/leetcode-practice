class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        """
        use two pointer to maintain a sliding window
        """
        j = -1 # left pointer
        _sum = 0
        ret = 9999999
        for i in range(len(nums)): # right pointer
            _sum = _sum + nums[i]
            while _sum >= target:
                ret = min(ret, i - j)
                j = j + 1
                _sum = _sum - nums[j]
                
        
        if ret == 9999999:
            return 0
        
        return ret
