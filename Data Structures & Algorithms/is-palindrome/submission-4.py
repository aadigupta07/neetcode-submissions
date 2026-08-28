class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(filtered) - 1
        while (left < right):
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        
        return True