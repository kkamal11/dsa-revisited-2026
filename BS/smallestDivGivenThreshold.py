import math


def divisorSum(nums, divisor):
    sum_ = 0
    for num in nums:
        sum_ += math.ceil(num / divisor)
    return sum_


def smallestDivisor(nums, thres):
    n = max(nums) + 1
    for i in range(1, n):
        sum_ = divisorSum(nums, i)
        if sum_ <= thres:
            return i


def smallestDivisorBinarySearch(nums, threshold):
    lo = 1
    hi = max(nums) + 1
    while lo < hi:
        mid = (lo + hi) // 2
        res = divisorSum(nums, mid)
        if res <= threshold:
            hi = mid
        else:
            lo = mid + 1
    return lo


nums = [1, 2, 5, 9]
threshold = 6

nums2 = [44, 22, 33, 11, 1]
threshold2 = 5
print(smallestDivisor(nums, threshold))
print(smallestDivisor(nums2, threshold2))
print(smallestDivisorBinarySearch(nums, threshold))
print(smallestDivisorBinarySearch(nums2, threshold2))
