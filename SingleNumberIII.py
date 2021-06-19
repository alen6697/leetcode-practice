class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.defaultdict(int)
        for n in nums:
            count[n] = count[n] + 1
            
        output = []
        for key in count:
            if count[key] == 1:
                output.append(key)
                
        return output
