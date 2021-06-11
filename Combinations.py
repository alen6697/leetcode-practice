class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []
        path = []
        self.dfs(n, path, 1, answer, k)
        
        return answer
    
    def dfs(self, n, path, index, answer, k):
        if len(path) == k:
            answer.append(list(path))
            return
        
        for i in range(index, n + 1):
            path.append(i)
            self.dfs(n, path, i + 1, answer, k)
            path.pop()
