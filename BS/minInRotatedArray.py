def find_min_in_rotated_arr(arr):
    """
    identify the sorted half -> eliminate left right
    if arr[low] < arr[mid] -> means this part is sorted because sorted array was rotated
    in that case the second part migt have the answer
    before discarding the half, pick the min from yhat
    and update our ans ->once min is picked discard it as its of no use
    """
    low = 0
    high = len(arr) - 1
    ans = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = min(ans, arr[mid])
            high = mid - 1
    return ans


arr1 = [3, 4, 5, 1, 2]
arr2 = [4, 5, 6, 7, 0, 1, 2]
arr3 = [18, 10, 13, 15, 17]
arr4 = [5, 1, 2, 3, 4]
print(min(arr1), find_min_in_rotated_arr(arr1))
print(min(arr2), find_min_in_rotated_arr(arr2))
print(min(arr3), find_min_in_rotated_arr(arr3))
print(min(arr4), find_min_in_rotated_arr(arr4))
