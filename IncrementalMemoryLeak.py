class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        i = 1
        while i <= memory1 or i <= memory2:
            if memory1 >= memory2:
                memory1 = memory1 - i
            else:
                memory2 = memory2 - i
                
            i = i + 1
            
        return [i, memory1, memory2]
