class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = [""]
        for c in s:
            tmp = []
            for o in output:
                if c.isalpha():
                    o1 = o + c.lower()
                    o2 = o + c.upper()
                    tmp.append(o1)
                    tmp.append(o2)
                else:
                    o = o + c
                    tmp.append(o)
                    
            output = list(tmp)
        
        return output
