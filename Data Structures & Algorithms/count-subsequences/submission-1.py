class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # like another index in each type of scenario
        # number of combinations using i letters from s to get t letteres from t
        if len(s) < len(t):
            return 0

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1

        # at any given index you add dp[i-1][j]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] += dp[i-1][j] # you can always add combo of not using new character
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[-1][-1]
