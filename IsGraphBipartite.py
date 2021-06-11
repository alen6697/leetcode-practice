class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        col = [-1] * len(graph)
        
        for i in range(len(graph)):
            if col[i] == -1:
                queue = []
                queue.append((i, 0))
            
                while queue:
                    node, color = queue.pop(0)
                    if col[node] == -1:
                        col[node] = color
                        for nx in graph[node]:
                            queue.append((nx, color ^ 1))
                            
                    if col[node] != color:
                        return False
                        
        return True
