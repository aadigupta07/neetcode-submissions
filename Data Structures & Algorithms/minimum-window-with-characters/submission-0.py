class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = Counter(t)

        ongoing = Counter()
        minimum = float('inf')

        working_l = -1
        working_r = -1
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in freq_t:
                ongoing[c] +=1
            if ongoing == freq_t:
                if r-l+1 < minimum:
                    working_l = l
                    working_r = r
                minimum = min(minimum, r-l + 1)
                while l < r and ongoing == freq_t:
                    if r-l+1 < minimum:
                        working_l = l
                        working_r = r
                    minimum = min(minimum, r-l + 1)
                    if s[l] in freq_t:
                        ongoing[s[l]] -= 1
                    l+=1
                    

        if working_l == -1:
            return ""
        return s[working_l:working_r+1]        
                    


        