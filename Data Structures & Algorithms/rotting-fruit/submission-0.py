class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # finding locations for rotten fruit and storing in a queue, since it will branch out from there
        # boolean condition checking if any new fruit have been rotted in most recent minute
        # count fresh fruit to check if all are rotted, in same pass as storing rotten
        queue = deque()
        fresh = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0: # if there were no fresh fruit to begin with
            return 0
        
        minutes = 0

        while queue:
            rotted = False

            for _ in range(len(queue)):
                r, c = queue.popleft()
                for a, b in ((0,1), (1, 0), (-1, 0), (0,-1)):
                    nr, nc = r + a, c + b
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        rotted = True
                        fresh -= 1

            minutes+=1
            if fresh == 0:
                return minutes
            if rotted == False:
                return -1
        
        return -1
            
            

            






