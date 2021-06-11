class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort() ## remove duplicated need to compare i and i - 1 so need to be sorted
        used = [False] * len(nums)
        self.dfs(nums, [], used, answer)
        
        return answer
    
    def dfs(self, nums, res, used, answer):
        if len(res) == len(nums):
            answer.append(list(res))
            return
        
        for i in range(len(nums)):
            if not used[i]:
                # the following check means two adjcent element are duplicated
                # we can ignore the duplicated one
                # if i - 1 is not taken, then i is not taken
                if i != 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                    
                res.append(nums[i])
                used[i] = True
                self.dfs(nums, res, used, answer)
                res.pop()
                used[i] = False
