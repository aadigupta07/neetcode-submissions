class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqS, freqT = Counter(s), Counter(t)
        for key in freqT:
            if freqT[key] != freqS[key]:
                return key
        
        return 'a'