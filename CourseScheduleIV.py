class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].add(prerequisite[0])
        
        output = [False] * len(queries)
        for i in range(len(queries)):
            end = queries[i][0]
            queue = []
            queue.append(queries[i][1])
            visited = [False] * numCourses
            visited[queries[i][1]] = True
            
            while queue:
                current = queue.pop(0)
                if current == end:
                    output[i] = True
                    break
                    
                for n in graph[current]:
                    if not visited[n]:
                        queue.append(n)
                        visited[n] = True
                        
        return output
