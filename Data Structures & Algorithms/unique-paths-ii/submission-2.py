class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = [[0] * len(obstacleGrid) for _ in range(len(obstacleGrid[0]))]
        # f(x, y) = f(x-1, y) + f(x, y-1)

        dp[0][0] = 1
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                else:
                    if i > 0:
                        dp[i][j]+=dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        
        return dp[len(dp)-1][len(dp[0])-1]