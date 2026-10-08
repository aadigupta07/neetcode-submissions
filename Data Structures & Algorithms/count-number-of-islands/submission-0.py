class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        

        def bfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] != "1":
                return
            
            grid[r][c] = "0"
            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        
        return count
