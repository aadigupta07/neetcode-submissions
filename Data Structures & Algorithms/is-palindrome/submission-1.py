class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = [c.lower() for c in s if c.isalnum()]
        return phrase == phrase[::-1]