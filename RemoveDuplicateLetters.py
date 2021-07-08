class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        lookup = set()
        last = {c: i for i, c in enumerate(s)}
        res = ""
        for i, c in enumerate(s):
            if c not in lookup:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    lookup.remove(stack.pop())
                lookup.add(c)
                stack.append(c)
        
        return "".join(stack)
