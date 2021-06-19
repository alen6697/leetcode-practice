class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        strHash = collections.defaultdict(int)
        for s in str:
            strHash[s] = strHash[s] + 1
            
        result = ""
        for o in order:
            if o in strHash:
                result = result + o * strHash[o]
                strHash.pop(o)
                
        for key in strHash:
            result = result + key * strHash[key]
            
        return result
