class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1 = self.convertInt(num1)
        n2 = self.convertInt(num2)
        sumN = n1 * n2
        
        return self.convertStr(sumN)
        
        
    def convertInt(self, num):
        power = 0
        s = 0
        for i in range(len(num) - 1, -1, -1):
            t = ord(num[i]) - 48
            s = s + t * (10 ** power)
            power = power + 1
            
        return s
    
    def convertStr(self, sumN):
        divisor = 10
        s = ""
        while sumN > 0:
            t = sumN % divisor
            sumN = sumN / 10
            s = s + chr(t + 48)
        
        return s[::-1]
