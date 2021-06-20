class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        
        result = []
        self.dfs(n, n, "", result) 
        # dfs(how many left parentheses can be used, how many right parentheses can be used, item, result)
        
        return result
    
    def dfs(self, leftCount, rightCount, item, result):
        if rightCount < leftCount: # right count < left connt means the parentheses is not well-formed
            return
        
        if leftCount == 0 and rightCount == 0: # the case means this is well-formed 
            result.append(item)
            
        if leftCount > 0:
            self.dfs(leftCount - 1, rightCount, item + "(", result)
            
        if rightCount > 0:
            self.dfs(leftCount, rightCount - 1, item + ")", result)
