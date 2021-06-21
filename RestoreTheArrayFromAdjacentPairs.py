class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        edges = collections.defaultdict(set)
        for u, v in adjacentPairs:
            edges[u].add(v)
            edges[v].add(u)
        
        start = None
        for e in edges:
            if len(edges[e]) == 1:
                start = e
                break
                
        ans = [start]
        previous = -100000000
        for i in range(len(adjacentPairs)):
            current = ans[-1]
            if previous in edges[current]:
                edges[current].remove(previous)
                
            gonext = list(edges[current])[0]
            ans.append(gonext)
            previous = current
            
        return ans
