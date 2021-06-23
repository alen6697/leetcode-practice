class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        
        print(result)
        if len(result) < k:
            return -1
        
        return result[k-1]
