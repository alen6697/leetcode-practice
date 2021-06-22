class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                s1 = s1 + c.lower()
                
        left = 0
        right = len(s1) - 1
        while left < right:
            if s1[left] != s1[right]:
                return False
            
            left = left + 1
            right = right - 1
            
        return True
