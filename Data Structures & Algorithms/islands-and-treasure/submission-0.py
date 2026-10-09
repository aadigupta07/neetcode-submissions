class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        INF = 2147483647
        while queue:
            r, c = queue.popleft()
            
            for a, b in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + a, c + b
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != INF: # either water, treasure, or already visited
                    continue
                else:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
            
                    
                

            

                    
                    
