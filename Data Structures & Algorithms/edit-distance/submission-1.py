class Solution:
    def minDistance(self, word1: str, word2: str) -> int:  
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # how many operations using i letters from word 1 to make j letters from word 2
        for i in range(len(word1)+1):
            dp[i][0] = i
        
        for j in range(len(word2) + 1):
            dp[0][j] = j

        # if word1[i] = word2[j], you don't need to increase operations, you can use dp[i-1][j-1]
        # if they aren't equal, its dp[i-1][j-1] + 1
        # dp[i-1][j] represents the number of changes to make j with one less character
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    dp[i][j] += 1
                    
                    
        return dp[-1][-1]
