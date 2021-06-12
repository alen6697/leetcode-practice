class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.size = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.size != len(self.stack):
            self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        
        return self.stack.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if len(self.stack) >= k:
            for i in range(k):
                self.stack[i] = self.stack[i] + val
        else:
            for i in range(len(self.stack)):
                self.stack[i] = self.stack[i] + val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
