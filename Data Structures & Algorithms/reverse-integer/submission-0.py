class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        if x < 0:
            multiplier = -1
        new = 0
        x = abs(x)
        while x != 0:
            new *= 10

            curr = x%10
            new += curr

            x//=10
        
        if new > 2**31 - 1 or new < (-2)**31:
            return 0
        return new * multiplier
