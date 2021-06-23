class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)): # start search from i and make i as middle point
            test = self.helper(i, i, s)  # case cbc 
            if len(test) > len(res):
                res = test
                
            test = self.helper(i, i + 1, s)  # case cbbc
            if len(test) > len(res):
                res = test
                
        return res
    
    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]: # start search from middle
            l = l - 1
            r = r + 1
            
        return s[l + 1: r] # i + 1 because loop stopped when l < 0. so if l < 0 then l need to add 1
