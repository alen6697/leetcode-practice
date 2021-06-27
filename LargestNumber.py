class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # recurrsive to permutate will be overflow
        # so we need to use non-recurrsive
        # idea is to compare each two element e.g. a + b > b + a or a + b < b + a
        # if a + b < b + a then we swap index of a and b
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                if self.getLargest(str(nums[j]), str(nums[j + 1])):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        return str(int("".join(map(str, nums))))
        
    def getLargest(self, a, b):
        if a + b >= b + a:
            return False
        elif a + b < b + a:
            return True
