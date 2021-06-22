class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        number = 0
        curSum = 0
        for i in range(len(arr)):
            if i < k:
                curSum = curSum + arr[i]
            else:
                if curSum / k >= threshold:
                    number = number + 1
                    
                curSum = curSum - arr[i-k]
                curSum = curSum + arr[i]
                
        if curSum / k >= threshold:
            number = number + 1
        
        return number
