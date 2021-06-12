class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dictS = collections.defaultdict(int)
        dictT = collections.defaultdict(int)
        
        for c in s:
            dictS[c] = dictS[c] + 1
        
        for cc in t:
            dictT[cc] = dictT[cc] + 1
         
        count = 0
        keys = list(set(dictS.keys() + dictT.keys()))
        for key in keys:
            count = count + (abs(dictS[key] - dictT[key]))
                
        return count / 2
