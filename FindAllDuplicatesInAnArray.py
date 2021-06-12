class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency = collections.defaultdict(int)
        for n in nums:
            frequency[n] = frequency[n] + 1
            
        result = []
        keys = frequency.keys()
        for key in keys:
            if frequency[key] > 1:
                result.append(key)
        
        return result
