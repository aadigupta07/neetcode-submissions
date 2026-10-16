class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        max_length = 0
        for word in wordDict:
            max_length = max(max_length, len(word))
        # stored longest string worth checking
        

        words = set(wordDict)
        # inefficnelty, going through each word in word dict each time, seeing if it branches from index, index is pushed if dp[index] is true
        
        for i in range(len(s) + 1):
            if dp[i]: # only worth extending a valid list
                for j in range(i+1, i+max_length+1):
                    if j > len(s):
                        break
                    
                    if s[i:j] in words:
                        dp[j] = True


        return dp[len(s)] # check if i should intialize with + 1 to return len(s)
