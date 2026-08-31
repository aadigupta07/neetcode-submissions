class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in s:
            freq1[c] += 1
        for c in t:
            freq2[c] += 1

        return freq1 == freq2