class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = [[False] * len(heights[0]) for _ in range(len(heights))]
        atl = [[False] * len(heights[0]) for _ in range(len(heights))]

        queue = deque()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0: # pacific
                    pac[i][j] = True
                    queue.append((i, j))
        
        while queue:
            r, c = queue.popleft()

            for a, b in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + a, c + b
                if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]):
                    continue
                
                if heights[nr][nc] >= heights[r][c] and not pac[nr][nc]:
                    pac[nr][nc] = True
                    queue.append((nr, nc))
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1 or j == len(heights[0])-1:
                    atl[i][j] = True
                    queue.append((i, j))
        
        while queue:
            r, c = queue.popleft()

            for a, b in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + a, c + b
                if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]):
                    continue
                
                if heights[nr][nc] >= heights[r][c] and not atl[nr][nc]:
                    atl[nr][nc] = True
                    queue.append((nr, nc))

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pac[i][j] and atl[i][j]:
                    result.append([i, j])
    
        return result
                    

        
            
