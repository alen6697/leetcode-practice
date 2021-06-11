class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        
        answer = []
        self.dfs(n, k, 1, [], answer)
        
        return answer
    
    def dfs(self, n, k, start, res, answer):
        if n < 0:
            return
        
        if n == 0 and len(res) == k:
            answer.append(list(res))
            return
            
        for i in range(start, 10):
            res.append(i)
            self.dfs(n - i, k, i + 1, res, answer)
            res.pop()
