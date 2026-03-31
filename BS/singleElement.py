def singleNonDuplicate(arr):
    hash_map = {}
    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1
    for k in hash_map:
        if hash_map[k] == 1:
            return k


def singleNonDuplicate2(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num
    return xor


def singleNonDuplicate3(arr):
    n = len(arr)
    # EDGE CASES
    ## When arr has only one elemnt
    if n == 1:
        return arr[0]
    ## I will exclude first and last element from binary search hence handling here
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Found the single element
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        # (even, odd) -> element is on right side: eliminate left
        # (odd, even) -> element is on left side: eliminate righ
        if (
            mid % 2 == 0
            and arr[mid + 1] == arr[mid]
            or mid % 2 != 0
            and arr[mid - 1] == arr[mid]
        ):
            # eliminate left
            low = mid + 1
        else:
            # eliminate right
            high = mid - 1
    return -1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
nums2 = [3, 3, 7, 7, 10, 11, 11]

print(singleNonDuplicate(nums))
print(singleNonDuplicate(nums2))
print(singleNonDuplicate2(nums))
print(singleNonDuplicate2(nums2))
print(singleNonDuplicate3(nums))
print(singleNonDuplicate3(nums2))
