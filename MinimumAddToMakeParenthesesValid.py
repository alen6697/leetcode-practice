class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        count = 0
        for p in s:
            if p == "(":
                count = count + 1
            if p == ")":
                if count == 0:
                    result = result + 1
                else:
                    count = count - 1
                
        return count + result
