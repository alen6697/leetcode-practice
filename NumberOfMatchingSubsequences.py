class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # create a hash lookup
        position = collections.defaultdict(list)
        for i in range(len(s)):
            position[s[i]].append(i)
        
        count = 0
        for word in words:
            prev = -1
            found = True
            for w in word:
                # binary search for each letter of element of words
                tmp = bisect.bisect(position[w], prev)
                if tmp == len(position[w]):
                    found = False
                    break
                else:
                    prev = position[w][tmp]
            if found:
                count = count + 1
                
        return count
