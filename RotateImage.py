class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        reverse it then transport it
        reverse:
            7 8 9
            4 5 6
            1 2 3
        then    
        transport:
            7 4 1
            8 5 2
            9 6 3
        """
        N = len(matrix)
        matrix.reverse()
        for r in range(N):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
