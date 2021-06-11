class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)
        for u, v in paths:
            graph[u].add(v)
            graph[v].add(u)
            
        res= [0] * (n + 1)
        for i in range(1, n + 1): # traverse all the node
            # check connected neighbors' color
            available={1, 2, 3, 4}
            for n in graph[i]: # traverse all neighbors of the node
                if res[n] in available: # if neighbor n has been colored by a number
                    available.remove(res[n])  # remove the number since we can't color by this number           
            res[i] = available.pop()  # color this node with the color which is different from neighbors
            
        return res[1:]
