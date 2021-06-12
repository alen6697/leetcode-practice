class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        output = []
        tmpTiles = list(tiles)
        tmpTiles.sort()
        tiles = "".join(tmpTiles)
        visited = [False] * len(tiles) 
        self.dfs(tiles, "", visited, output)
        
        return len(output)
    
    def dfs(self, tiles, res, visited, output):
        if len(res) == len(tiles):
            return
        
        for i in range(len(tiles)):
            if i != 0 and tiles[i] == tiles[i-1] and not visited[i-1]:
                continue
                
            if not visited[i]:    
                res = res + tiles[i]
                visited[i] = True
                output.append(res)
                self.dfs(tiles, res, visited, output)
                res = res[:-1]
                visited[i] = False
