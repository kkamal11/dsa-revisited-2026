def findPeakElement(nums):
    n = len(nums)
    if n == 1:
        return 0
    peak = 0
    for i in range(n):
        if (i == 0 and nums[i] > nums[i + 1]) or (i == n - 1 and nums[i] > nums[i - 1]):
            peak = i
        else:
            if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
                return i
    return peak


def findPeakElement2(nums):
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    lo = 1
    hi = len(nums) - 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid - 1] < nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


nums = [1, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
nums3 = [1, 2, 3, 5, 6, 7]
nums4 = [7, 6, 5, 4, 3, 2, -1]
print(findPeakElement(nums))
print(findPeakElement(nums2))
print(findPeakElement(nums3))
print(findPeakElement(nums4))
print("=" * 10)
print(findPeakElement2(nums))
print(findPeakElement2(nums2))
print(findPeakElement2(nums3))
print(findPeakElement2(nums4))
