class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = n * -1
            
        result = 1
        while n:
            if n & 1:  # get lowest bit
                result = result * x
                
            x = x * x
            n = n >> 1 # shift n because we want to get lowest bit
            
        return result
