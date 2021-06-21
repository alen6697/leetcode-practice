class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        tmp = list(s)
        for i in range(len(s)):
            if s[i] == "(": # if s[i] is (, push index to stack
                stack.append(i)
                
            if s[i] == ")":  # if s[i] is )
                if not stack:  # if stack is empty, remove this )
                    tmp[i] = " "
                else:  # if stack is not empty, pop a (
                    stack.pop()
                    
        while stack:  # if stack has some ( left, we remove all of them
            tmp[stack.pop()] = " "
            
        result = ""
        for c in tmp:
            if c != " ":
                result = result + c
                
        return result
