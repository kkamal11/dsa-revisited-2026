def how_many_times_array_is_rotated(arr):
    """index of min elemtn tells how many times arr is rotated"""
    rotation = 0
    min_ = float("inf")
    for i in range(len(arr)):
        if min_ > arr[i]:
            min_ = arr[i]
            rotation = i
    return rotation


def how_many_times_array_is_rotated2(arr):
    n = len(arr)
    if n == 1:
        return 1
    for i in range(n - 1):
        if arr[i + 1] < arr[i]:
            return i + 1


def how_many_times_array_is_rotated3(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        # If mid element is greater than element at high,
        # smallest element lies to the right of mid
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            # Else smallest element is at mid or to the left
            high = mid
    return low


arr = [4, 5, 6, 7, 0, 1, 2, 3]
arr2 = [3, 4, 5, 1, 2]

print(how_many_times_array_is_rotated(arr))
print(how_many_times_array_is_rotated(arr2))
print(how_many_times_array_is_rotated2(arr))
print(how_many_times_array_is_rotated2(arr2))
print(how_many_times_array_is_rotated3(arr))
print(how_many_times_array_is_rotated3(arr2))
