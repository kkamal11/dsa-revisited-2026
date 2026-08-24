class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(c):
            for j in range(c):
                if i ** 2 + j ** 2 == c:
                    return True
        return False
    