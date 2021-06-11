class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        output = []
        for qx, qy, qr in queries:
            count = 0
            for px, py in points:
                if (px - qx) * (px - qx) + (py - qy) * (py - qy) <= (qr * qr):
                    count = count + 1
                    
            output.append(count)
            
        return output
