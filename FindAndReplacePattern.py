class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        p = self.getPattern(pattern)
        for word in words:
            if self.getPattern(word) == p:
                output.append(word)
        
        return output
    
    def getPattern(self, pattern):
        lookup = {}
        out = []
        
        encode = 0
        for p in pattern:
            if p not in lookup:
                encode = encode + 1
                lookup[p] = encode
                
            out.append(lookup[p])
                
        return out
