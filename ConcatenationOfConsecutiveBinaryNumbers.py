class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumStr = ""
        for i in range(1, n + 1):
            sumStr = sumStr + bin(i)[2:]
            
        return int(sumStr, 2) % (10 ** 9 + 7)
