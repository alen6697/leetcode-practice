class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) == 1:
            return s1 in s2
        
        
        s1map = collections.defaultdict(int)
        for s in s1:
            s1map[s] = s1map[s] + 1
        
        last = len(s1)
        for i in range(len(s2) - last + 1):
            s2map = collections.defaultdict(int)
            for j in range(i, i + last):  # sliding window to build dict by s2
                s2map[s2[j]] = s2map[s2[j]] + 1
            
            if s1map == s2map: # check if two dicts are same 
                return True
            
        return False
