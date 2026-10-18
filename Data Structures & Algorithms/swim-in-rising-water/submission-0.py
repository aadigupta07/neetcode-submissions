class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maximum = [[float('inf')] * n for _ in range(n)]
        maximum[0][0] = grid[0][0]
        # equivalent of dist in djikstras
        heap = [(grid[0][0], 0, 0)]
        # best max elevation to reach cell, r, c format


        while heap:
            height, r, c = heapq.heappop(heap)

            if height > maximum[r][c]: # already found a way to make it to grid[r][c] with a smaller max
                continue
            
            for a, b in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + a, b + c
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid):
                    continue
                new_max = max(height, grid[nr][nc])

                if new_max < maximum[nr][nc]:
                    maximum[nr][nc] = new_max
                    heapq.heappush(heap, (new_max, nr, nc))
                
                

        return maximum[-1][-1]
                



        

            

