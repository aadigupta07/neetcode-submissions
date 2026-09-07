from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = Counter(t)
        required = len(freq_t)  # number of distinct chars that must be satisfied

        ongoing = Counter()
        formed = 0  # number of distinct chars currently satisfied

        minimum = float('inf')
        working_l, working_r = -1, -1
        l = 0

        for r in range(len(s)):
            c = s[r]
            if c in freq_t:
                ongoing[c] += 1
                if ongoing[c] == freq_t[c]:
                    formed += 1 # this formed tactic makes more sense, easier to check, you can look at failed submission for comparison, since you need AT LEAST however many characters, not exactly that many

            while l <= r and formed == required:
                if r - l + 1 < minimum:
                    minimum = r - l + 1
                    working_l, working_r = l, r

                left_c = s[l]
                if left_c in freq_t:
                    if ongoing[left_c] == freq_t[left_c]:
                        formed -= 1
                    ongoing[left_c] -= 1
                l += 1

        return "" if working_l == -1 else s[working_l:working_r + 1] # check you hit anything

        