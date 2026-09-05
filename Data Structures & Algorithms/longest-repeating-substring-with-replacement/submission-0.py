class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = Counter()
        longest = 0
        start = 0

        for end in range(len(s)):
            c = s[end]
            counts[c] += 1
            window = end-start + 1
            if window - counts.most_common(1)[0][1] > k:
                counts[s[start]] -=1
                start +=1

            longest = max(longest, end-start + 1)
        
        return longest
            
