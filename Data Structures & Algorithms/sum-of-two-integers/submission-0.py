class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask
        while b != 0:
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = sum_without_carry, carry
    # if a's 32nd bit is set, it's negative in two's complement — convert back
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a