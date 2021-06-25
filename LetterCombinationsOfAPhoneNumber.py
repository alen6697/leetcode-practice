class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        digitsMap = {'2': 'abc', '3': 'def', '4': 'ghi', 
                     '5': 'jkl', '6': 'mno', '7': 'pqrs', 
                     '8': 'tuv', '9': 'wxyz'}
    
        output = [""]
        for digit in digits:
            tmp = []
            for v in digitsMap[digit]:
                for o in output:
                    tmp.append(o + v)  # get all element in output and concat v
                    
            output = tmp
        
        return output
