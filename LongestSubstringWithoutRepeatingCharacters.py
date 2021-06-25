class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result = 0
        lookup = collections.defaultdict(int)
        for i in range(len(s)):
            lookup[s[i]] = lookup[s[i]] + 1
            while lookup[s[i]] > 1:  # if frequency of s[i] is greater than 1, s[start] subtract 1 and move start to next
                lookup[s[start]] = lookup[s[start]] - 1 # s[start] subtract 1 because we got duplicate letter 
                start = start + 1                       # so we want to move start to next one
                
            result = max(result, i - start + 1)
            
        return result
