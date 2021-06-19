class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        knowledgeMap = {}
        for k in knowledge:
            knowledgeMap[k[0]] = k[1]
            
        prev = 0
        arr = []
        for i in range(len(s)):
            if s[i] == "(":
                arr.append(s[prev:i])
                prev = i + 1
                continue
            
            if s[i] == ")":
                k = s[prev:i]
                if k in knowledgeMap:
                    arr.append(knowledgeMap[k])
                else:
                    arr.append("?")
                    
                prev = i + 1
                
        arr.append(s[prev:])
        
        return "".join(arr)
