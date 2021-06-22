class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        # keep a max number as running
        # if i + 1 == running then all bulbs are blue
        count = 0
        running = 0
        for i in range(len(light)):
            running = max(running, light[i])
            if i + 1 == running:
                count = count + 1
                
        return count
