class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        """
        x x x   a
        x x x   b
        x x x   c
        
        x y z
        
        a+b+c = x+y+z
        """
        # initial result
        resultRow = [0] * len(colSum)
        result = [list(resultRow) for _ in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] = rowSum[i] - result[i][j]
                colSum[j] = colSum[j] - result[i][j]
                
        return result
