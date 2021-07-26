class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordCount = collections.defaultdict(int)
        for c in s:
            wordCount[c] = wordCount[c] + 1
        
        count = 0
        oddFound = False
        for k, v in wordCount.items():
            if oddFound:
                if wordCount[k] > 1:
                    if wordCount[k] % 2 == 0:
                        count = count + wordCount[k]
                    else:
                        count = count + (wordCount[k] - 1)    
            else:
                if wordCount[k] % 2 == 0:
                    count = count + wordCount[k]
                else:
                    count = count + wordCount[k]
                    oddFound = True
        
                
        return count
