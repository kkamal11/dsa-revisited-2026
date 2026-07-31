from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        for k in d:
            if d[k] == 1:
                return k

    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for bit in range(32):
            count = 0

            for num in nums:
                if num & (1 << bit):
                    count += 1

            if count % 3:
                ans |= 1 << bit

        # Convert from unsigned 32-bit representation
        # to Python's negative integer if sign bit is set.
        if ans >= (1 << 31):
            ans -= 1 << 32

        return ans
