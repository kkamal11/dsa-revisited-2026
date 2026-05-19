"""
Given an integer array nums, rotate the array to the right by k
steps, where k is non-negative.

Examples:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [1,2,3,4,5,6,7], k = 2
Output: [3,4,5,6,7,1,2]
"""


class RotateArrayUtil:
    @staticmethod
    def rotate_array_right(nums, k):
        k = k % len(nums)
        return nums[-k:] + nums[:-k]

    @staticmethod
    def rotate_array_left(nums, k):
        k = k % len(nums)
        return nums[:-k] + nums[:k]

    @staticmethod
    def rotate_array_right2(nums, k):
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        n = len(nums)

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

        return nums

    @staticmethod
    def rotate_array_left2(nums, k):
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        n = len(nums)

        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        reverse(nums, 0, n - 1)

        return nums
