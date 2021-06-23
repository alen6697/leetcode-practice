class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "" or s == "-" or s =="+":
            return 0
        
        s1 = re.match("[^\d]+", s.lstrip("-").lstrip("+"))
        
        if s1 != None:
            return 0
        else:
            s1 = re.search("\-*\+*\d+", s).group()
            
        if s1[:2] == "--" or s1[:2] == "-+" or s1[:2] == "++":
            return 0
        
        ss = int(s1)
        if ss > 2**31 - 1:
            return 2**31 -1
        if ss < -1 * (2**31):
            return -1 * (2**31)
        
        return ss
