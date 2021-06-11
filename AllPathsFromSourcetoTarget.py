class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        
        output = []
        self.searchTarget(0, [0], output, graph)
        
        return output
        
    def searchTarget(self, node, path, output, graph):
        if node == len(graph) - 1:
            output.append(path)
            
        for n in graph[node]:
            self.searchTarget(n, path + [n], output, graph)
        
