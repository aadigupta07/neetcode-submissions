class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for i in range(n)]
        count = 1
        row, column = 0 , 0
        while count <= n**2:
            while column < n and grid[row][column] == 0: # right
                grid[row][column] = count
                count +=1
                column +=1
            column -=1
            row +=1
            
            while row < n and grid[row][column] == 0: # down
                grid[row][column] = count
                count +=1
                row +=1
            row -=1
            column -=1
            
            while column >= 0 and grid[row][column] == 0: # left
                grid[row][column] = count
                count +=1
                column -=1
            column +=1
            row -=1

            while row >= 0 and grid[row][column] == 0: # up
                grid[row][column] = count
                count +=1
                row -=1
            row +=1
            column +=1
        return grid
            