class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num = [1]
        i2 = i3 = i5 = 0

        for _ in range(1, n):
            next_ugly = min(ugly_num[i2] * 2, ugly_num[i3] * 3, ugly_num[i5] * 5)
            ugly_num.append(next_ugly)

            if next_ugly == ugly_num[i2] * 2:
                i2 += 1
            if next_ugly == ugly_num[i3] * 3:
                i3 += 1
            if next_ugly == ugly_num[i5] * 5:
                i5 += 1
        return ugly_num[-1]
