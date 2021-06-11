class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        candidates.sort() # remove duplicated need to compare i and i - 1 so need to be sorted
        self.dfs(candidates, target, [], answer, 0)
        
        return answer
    
    def dfs(self, candidates, target, res, answer, index):
        if target < 0:
            return
        
        if target == 0:
            answer.append(list(res))
            return
        
        for i in range(index, len(candidates)):
            # the following check means two adjcent element are duplicated
            # we can ignore the duplicated one
            if i != index and candidates[i] == candidates[i-1]:
                continue
                
            res.append(candidates[i])
            self.dfs(candidates, target - candidates[i], res, answer, i + 1)
            res.pop()
