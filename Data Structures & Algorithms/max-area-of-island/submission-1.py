class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.area = 0

        def bfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            self.area+=1
            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs(i, j)
                    max_area = max(max_area, self.area)
                    self.area = 0
        
        return max_area