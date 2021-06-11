class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        array = [x + 1 for x in range(m)]
        output = []
        
        for i in range(len(queries)):
            index = array.index(queries[i])
            output.append(index)
            array = [queries[i]] + array[:index] + array[index+1:]
        
        return output
