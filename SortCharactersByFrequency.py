class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = collections.defaultdict(int)
        for i in s:
            frequency[i] = frequency[i] + 1
            
        reverseFrequency = collections.defaultdict(list)
        for key in frequency:
            reverseFrequency[frequency[key]].append(key)
            
        keys = reverseFrequency.keys()
        keys.sort(reverse=True)
        res = ""
        for key in keys:
            for c in reverseFrequency[key]:
                res = res + c * key
            
        return res
