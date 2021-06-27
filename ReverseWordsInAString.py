class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = []
        tmp = ""
        for c in s:
            if c != " ":
                tmp = tmp + c
            else:    
                if tmp:
                    sList.append(tmp)
                    tmp = ""
        
        sList.append(tmp)
        res = ""
        for i in range(len(sList) - 1, -1, -1):
            res = res + sList[i]
            res = res + " "
            
        res = res.strip()
        
        return res
