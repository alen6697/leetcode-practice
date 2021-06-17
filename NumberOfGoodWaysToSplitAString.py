class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        goodSplit = 0
        left = [0] * 26
        right = [0] * 26
        for i in range(len(s)):  # assign all char frequency in right
            idx = ord(s[i]) - 97
            right[idx] = right[idx] + 1
            
        for i in range(len(s)):  # start spliting string so left + 1 then right need to be - 1
            idx = ord(s[i]) - 97
            left[idx] = left[idx] + 1
            right[idx] = right[idx] - 1
            
            distinctLeft = self.getDistinct(left)   # get frequency in left string
            distinctRight = self.getDistinct(right)  # get frequency in right string
            
            if distinctLeft == distinctRight:
                goodSplit = goodSplit + 1
                
        return goodSplit
    
    def getDistinct(self, count):
        c = 0
        for i in count:
            if i != 0:
                c = c + 1
                
        return c
