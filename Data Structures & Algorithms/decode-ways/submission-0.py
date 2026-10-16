class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * len(s)
        if s[0] == '0':
            return 0
        
        dp[0] = 1


        # if number is not 0, all past combinations still apply, cuz you can just chuck the number on the end of each combination
        # dp[i] = dp[i-1]
        # you add one if the last two numbers are compatible


        # if number is 0, and last 2 are not compatible, then no combinations are comptabile, so every dp[i] moving forward is 0
        # if number is 0, only other case is last two are compatible (meaning 1 or 2 for penultimate number), in which case dp[i] = dp[i-1] since last two values essentially become one unit in every viable case
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                else:
                    dp[i] = dp[i-1]
            
            else:
                dp[i] += dp[i-1]
                if s[i-1] == '0': # one instance of last two not compatible
                    continue
                if 1 <= int(s[i-1: i+1]) <= 26:
                    dp[i] += 1
        
        return dp[len(s)-1]
                
                
        
