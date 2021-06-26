class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicated = 0
        dupNum = 1
        i = 0
        while i < len(nums) - 1 and nums[i] != "_":        
            if nums[i] == nums[i + 1]:
                dupNum = dupNum + 1
            else:
                dupNum = 1
                    
            if dupNum > 2:
                k = i + 1
                duplicated = duplicated + 1
                dupNum = dupNum - 1
                while k < len(nums) - 1:
                    nums[k] = nums[k + 1]
                    k = k + 1
                    
                nums[-1] = "_"
                    
                if nums[i] != nums[i + 1]:
                    dupNum = 1
                    i = i + 1
            else:
                i = i + 1
                        
        return len(nums) - duplicated
