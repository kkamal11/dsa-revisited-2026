class Solution:
    def move_zeros(self, nums):
        n = len(nums)
        res = [0] * n
        insertIdx = 0

        for num in nums:
            if num != 0:
                res[insertIdx] = num
                insertIdx += 1

        return res

    def move_zeros_optimized(self, nums):
        insertIdx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[insertIdx], nums[i] = nums[i], nums[insertIdx]
                insertIdx += 1

        return nums


sol = Solution()
nums = [0, 1, 0, 3, 12]  # [1, 3, 12, 0, 0]
print(sol.move_zeros(nums))
nums = [0, 0, 1, 0, 0, 0, 3, 12]  # [1, 3, 12, 0, 0, 0, 0, 0]
print(sol.move_zeros(nums))
print(sol.move_zeros_optimized(nums))
