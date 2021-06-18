class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # we want to split to k palindrome string
        # so odd char should be less or equal to k
        if k > len(s):
            return False
        
        frequency = collections.defaultdict(int)
        for c in s:
            frequency[c] = frequency[c] + 1
            
        odds = 0
        for key in frequency:
            odds = odds + (frequency[key] % 2)
            
        return odds <= k
