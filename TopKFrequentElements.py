class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = collections.defaultdict(int)
        for num in nums:
            frequency[num] = frequency[num] + 1
            
        reverseFrequency = collections.defaultdict(list)
        for key in frequency:
            reverseFrequency[frequency[key]].append(key)
            
        keys = reverseFrequency.keys()
        keys.sort(reverse=True)
        result = []
        for key in keys:
            result = result + reverseFrequency[key]
            if len(result) == k:
                break
                
        return result
