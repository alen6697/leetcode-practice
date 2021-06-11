class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        res = []
        self.dfs(candidates, target, res, answer, 0)
        
        return answer
    
    def dfs(self, candidates, target, res, answer, start):
        if target < 0:
            return
        
        if target == 0:
            answer.append(list(res))
            return
        
        for i in range(start, len(candidates)):
            res.append(candidates[i])
            self.dfs(candidates, target - candidates[i], res, answer, i)
            res.pop()
