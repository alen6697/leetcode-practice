class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] = indegree[prerequisite[0]] + 1
            
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            c = queue.pop(0)
            for prerequisite in prerequisites:
                if indegree[prerequisite[0]] != 0:
                    if prerequisite[1] == c:
                        indegree[prerequisite[0]] = indegree[prerequisite[0]] - 1
                        
                    if indegree[prerequisite[0]] == 0:
                        queue.append(prerequisite[0])
                        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return False
            
        return True
