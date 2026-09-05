class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        start = 0
        recent = defaultdict(lambda: -1)
        longest = 0

        for end in range(len(s)):
            c = s[end]
            if recent[c] >= start:
                start = recent[c] + 1
            
            recent[c] = end


            longest = max(longest, end-start + 1)



        return longest
