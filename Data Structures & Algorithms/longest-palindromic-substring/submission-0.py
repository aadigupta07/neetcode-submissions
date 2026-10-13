class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = -1
        best_end = -2

        for i in range(len(s)):
            # start with single center check
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best_end - best_start + 1:
                    best_start = l
                    best_end = r
                l-=1
                r+=1

            # double center check
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best_end - best_start + 1:
                    best_start = l
                    best_end = r
                l-=1
                r+=1
                    

        return s[best_start:best_end+1]