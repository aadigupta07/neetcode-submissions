class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = Counter()
        longest = 0
        start = 0
        max_count = 0

        for end in range(len(s)):
            c = s[end]
            counts[c] += 1
            max_count = max(max_count, counts[c]) # More intuitive way would be less efficient but it would use counts.most_common. The current way knows that there is no point checking a smaller window
            window = end-start + 1
            if window - max_count > k: # <- window needs to grow
                counts[s[start]] -=1
                start +=1

            longest = max(longest, end-start + 1)
        
        return longest
            
