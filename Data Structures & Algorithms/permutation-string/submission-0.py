class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        freq_s1 = Counter(s1)
        ongoing_freq = Counter()

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            ongoing_freq[c] +=1
            if r-l + 1 < k:
                continue
            else:
                if freq_s1 == ongoing_freq:
                    return True
                ongoing_freq[s2[l]] -=1
                if ongoing_freq[s2[l]] == 0:
                    del ongoing_freq[s2[l]]
                
                l+=1
        
        return False
            

