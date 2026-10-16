class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp[i][j] represents the longest subsequence up to index i in text1 and index j in text2
        # cat crabt

        dp = [[0] * len(text2) for _ in range(len(text1))]
        

        
        for i in range(len(text1)):
            for j in range(len(text2)):
                max1 = 0
                max2 = 0
                if i > 0:
                    max1 = dp[i-1][j]
                if j > 0:
                    max2 = dp[i][j-1]
                if text1[i] == text2[j]:
                    if j > 0 and i > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(max1, max2)
        
        return dp[len(text1)-1][len(text2)-1]


        