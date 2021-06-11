class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        edges = [set() for _ in range(n)]
        indegree = [0] * n
        
        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                edges[i].add(leftChild[i])
                indegree[leftChild[i]]  = indegree[leftChild[i]] + 1
                
        for j in range(len(rightChild)):
            if rightChild[j] != -1:
                edges[j].add(rightChild[j])
                indegree[rightChild[j]]  = indegree[rightChild[j]] + 1
        
        start = -1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                start = i
                
        queue = []
        queue.append(start)
        
        visited = [False] * n
        visited[start] = True
        
        while queue:
            node = queue.pop(0)
            for e in edges[node]:
                if visited[e] == False:
                    queue.append(e)
                    visited[e] = True
                else:
                    return False
                
        for v in visited:      
            if not v:
                return False
            
        return True
