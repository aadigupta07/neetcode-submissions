class Solution:
    def checkValidString(self, s: str) -> bool:
        num_lefts = 0
        num_rights = 0
        wildcards = 0
        for c in s:
            if c == "(":
                num_lefts+=1
            elif c == ")":
                num_rights +=1
            else:
                wildcards+=1
            if num_rights > num_lefts + wildcards:
                return False
        
        if wildcards < abs(num_rights - num_lefts):
            return False
        return True