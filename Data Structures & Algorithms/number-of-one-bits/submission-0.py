class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1   # check if the last bit is 1
            n >>= 1          # shift right to look at the next bit
        return count