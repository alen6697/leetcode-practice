class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        center = -1
        for i in range(len(edges) - 1):
            if edges[i][0] in edges[i + 1]:
                center = edges[i][0]
                        
            if edges[i][1] in edges[i + 1]:
                center = edges[i][1]
                        
        return center
