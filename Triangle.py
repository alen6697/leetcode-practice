class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # add min of next level to current level
        for i in range(len(triangle) - 2, -1, -1):
            for c in range(i + 1):
                triangle[i][c] = triangle[i][c] + min(triangle[i + 1][c], triangle[i + 1][c + 1]) 
                
        return triangle[0][0]
