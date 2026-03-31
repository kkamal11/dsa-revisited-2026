import math


def findEatingTime(arr, rate):
    time = 0
    for b in arr:
        time += math.ceil(b / rate)
    return time


def minEatingSpeed(piles, h):
    n = max(piles) + 1
    for k in range(1, n):
        # This linear search can be optimized using binary search, but for simplicity, we are using a linear search here.
        t = findEatingTime(piles, k)
        if t <= h:
            return k


def minEatingSpeedBinarySearch(piles, h):
    lo = 1
    hi = max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        t = findEatingTime(piles, mid)
        # t hold the total time it would take to finish banana
        if t <= h:  # t > h means too slow time is high u need to increae rate(k)
            hi = mid
        else:
            lo = mid + 1
    return hi


piles = [3, 6, 7, 11]
h = 8
piles2 = [30, 11, 23, 4, 20]
h2 = 5
print(minEatingSpeed(piles, h))
print(minEatingSpeed(piles2, h2))
print(minEatingSpeedBinarySearch(piles2, h2))
