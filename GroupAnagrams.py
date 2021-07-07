class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        sort the string then put it in dictionary
        same group has same key in dictionary after sort
        """
        if len(strs) <= 0:
            return strs
        
        result = collections.defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            sortS = "".join(sorted(s))
            result[sortS].append(s)
            
        return result.values()
