class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for row in matrix: 
            l = l + row
            
        l.sort()
        
        return l[k - 1]
