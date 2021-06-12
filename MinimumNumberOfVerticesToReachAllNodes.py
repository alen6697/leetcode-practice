class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        output = set()
        graph = [set() for _ in range(n)]
        
        indegree = [0] * n
        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegree[edge[1]] = indegree[edge[1]] + 1
        
        queue = []
        visited = [False] * n
        for i in range(len(indegree)):
            if indegree[i] == 0:
                output.add(i)
                queue.append(i)
                visited[i] = True

        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                
        for i in range(len(visited)):
            if not visited[i]:
                output.add(i)
                        
        return list(output)
