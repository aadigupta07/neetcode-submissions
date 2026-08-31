class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = [c.lower() for c in s if c.isalnum()]
        st = "".join(phrase)
        left, right = 0, len(st)-1
        while left < right:
            if st[left] != st[right]:
                return False
            left += 1 
            right -= 1
        
        return True