class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        balance = k - n
        while balance > 0:
            if balance > 25:
                balance = balance - 25
                result = result + "z"
                n = n - 1
            else:
                result = result + chr(97 + balance)
                n = n - 1
                while n > 0:
                    result = result + "a"
                    n = n - 1
                    
                break
                
        return result[::-1]
