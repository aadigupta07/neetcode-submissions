class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i assume s1 is index in s1, index 2 is in s2
        # for each dp, check True for making i+j characters from s3 formed using i from s1 and j from s2
        # Main issue is number of substrings
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) +1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(len(s1)):
            if s1[i] == s3[i] and dp[i][0]:
                dp[i+1][0] = True

        for j in range(len(s2)):
            if s2[j] == s3[j] and dp[0][j]:
                dp[0][j+1] = True

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        
        return dp[-1][-1]
                    

                