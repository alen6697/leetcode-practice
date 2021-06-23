class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = collections.defaultdict(list)
        for i, n in enumerate(nums):
            hashMap[n].append(i)
            
        for key in hashMap:
            if target - key in hashMap:
                if key == target - key:
                    return hashMap[target - key]
                
                return [hashMap[key][0], hashMap[target - key][0]]
            
        return []
