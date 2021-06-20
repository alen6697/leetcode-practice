class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.score(s, 0, len(s) - 1)
    
    def score(self, s, start, end):
        if end - start == 1: # start is ( and end is )
            return 1
        
        balance = 0
        for i in range(start, end):
            if s[i] == '(':
                balance = balance + 1
            if s[i] == ')':
                balance = balance - 1
                
            if balance == 0: # balance
                # score("(A)(B)(C)") = score("(A)") + score("(B)(C)")
                return self.score(s, start, i) + self.score(s, i + 1, end)
        
        # score("(A)") = 2 * score("A")
        return 2 * self.score(s, start + 1, end - 1)
