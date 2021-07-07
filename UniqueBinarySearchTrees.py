class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        root.            1    +    2    +    3
                       /   \     /   \     /   \
        tree count    0     2   1     1   2     0
        
        """
        memory = {}
        return self.helper(1, n, n, memory)
    
    def helper(self, start, end, n, memory):
        if start < 1 or end > n or start >= end:
            return 1
        
        count = 0
        if (start, end) in memory:
            return memory[(start, end)]
        else:
            for i in range(start, end + 1):
                count = count + (self.helper(start, i - 1, n, memory) * self.helper(i + 1, end, n, memory))

            memory[(start, end)] = count
            return count
