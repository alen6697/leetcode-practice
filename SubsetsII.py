class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        if len(nums) == 0:
            return output
        
        nums.sort()
        output.append([])
        self.dfs(nums, [], 0, output)
        
        return output
    
    def dfs(self, nums, res, index, output):
        if len(res) == len(nums):
            return
        
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
                
            res.append(nums[i])
            output.append(list(res))
            self.dfs(nums, res, i + 1, output)
            res.pop()
