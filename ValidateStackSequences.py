class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # check if top of stack equals to first popped element
        stack = []
        for i in range(0, len(pushed)):
            stack.append(pushed[i]) # push each element of pushed to stack
            while stack and stack[-1] == popped[0]: # if top of stack equals to popped[0] then keep popping
                stack.pop()
                popped.pop(0)
                
        return len(popped) == 0
