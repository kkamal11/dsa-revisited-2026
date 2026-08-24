class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(c):
            for j in range(c):
                if i**2 + j**2 == c:
                    return True
        return False

    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = c

        while left <= right:
            val = left**2 + right**2
            if val == c:
                return True
            if val < c:
                left += 1
            else:
                right -= 1
        return False


def judgeSquareSum(self, c: int) -> bool:
    """
    Why right as int(c**0.5)?
    Because if c = 5, then the maximum value of a or b is 2,
    since 2^2 + 2^2 = 8 > 5. So we can limit the right pointer to
    int(c**0.5).
    """
    left = 0
    right = int(c**0.5)

    while left <= right:
        val = left**2 + right**2
        if val == c:
            return True
        if val < c:
            left += 1
        else:
            right -= 1
    return False
