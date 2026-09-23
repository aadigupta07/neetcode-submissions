class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1          # make room for the next bit
            result |= n & 1       # append n's last bit to result
            n >>= 1               # move to the next bit of n
        return result