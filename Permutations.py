class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        answer = []
        used = [False] * len(nums)
        self.dfs(nums, [], used, answer)
        
        return answer
        
    def dfs(self, nums, res, used, answer):
        if len(res) == len(nums):
            answer.append(list(res))
            return
            
        for i in range(len(nums)):
            if not used[i]:
                res.append(nums[i])
                used[i] = True
                self.dfs(nums, res, used, answer)
                res.pop()
                used[i] = False
