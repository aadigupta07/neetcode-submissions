class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0  # min and max possible number of unmatched '('
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:  # '*' could be ')', empty, or '('
                lo -= 1
                hi += 1
            if hi < 0:      # even treating every * as '(' there are too many ')'
                return False
            lo = max(lo, 0)  # can't have a negative open count
        return lo == 0