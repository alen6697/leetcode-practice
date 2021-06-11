class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if len(nums) == 0:
            return answer
        
        res = []
        answer.append(list(res))
        self.dfs(nums, len(nums), 0, res, answer)
        
        return answer
    
    def dfs(self, nums, length, index, res, answer):
        if len(res) == length:
            return
        
        for i in range(index, length):
            res.append(nums[i])
            answer.append(list(res))
            self.dfs(nums, length, i + 1, res, answer)
            res.pop()
