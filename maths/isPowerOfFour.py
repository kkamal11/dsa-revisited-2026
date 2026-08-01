class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1

    """
    Bit manipulation (interview favorite)

    A power of 4 satisfies:
    1. It is a power of 2 (only one bit set).
    2. That bit is in an even position (0, 2, 4, ...)
    """

    def isPowerOfFourBitManipulation(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
