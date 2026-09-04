class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[-1]
        for i in range(n):
            maxi = max(maxi, nums[i])
            mini = min(nums[i:])
            if maxi - mini <= k:
                return i

        return -1

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        maxi = nums[0]

        for i in range(n):
            maxi = max(maxi, nums[i])
            if maxi - suffix_min[i] <= k:
                return i

        return -1
