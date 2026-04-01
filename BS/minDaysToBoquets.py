def canMakeBoque(bloomDay, m, k, day):
    count = 0
    boquet_count = 0
    for b in bloomDay:
        if b <= day:
            count += 1
        else:
            boquet_count += count // k
            count = 0
    boquet_count += count // k
    return boquet_count >= m


def minDays(bloomDay, m, k):
    n = len(bloomDay)

    for day in range(min(bloomDay), max(bloomDay) + 1):
        if canMakeBoque(bloomDay, m, k, day):
            return day
    return -1


def minDaysBinary(bloomDay, m, k):
    n = len(bloomDay)
    if n < m * k:
        return -1
    lo = min(bloomDay)
    hi = max(bloomDay) + 1
    can_make = False
    while lo < hi:
        day = (lo + hi) // 2
        if canMakeBoque(bloomDay, m, k, day):
            can_make = True
            hi = day
        else:
            lo = day + 1
    return hi if can_make else -1


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
bloomDay2 = [7, 7, 7, 7, 12, 7, 7]
m2 = 2
k2 = 3

bloomDay3 = [1, 10, 3, 10, 2]
m3 = 3
k3 = 2

bloomDay4 = [1000000000, 1000000000]
m4 = 1
k4 = 1
print(minDays(bloomDay, m, k))
print(minDays(bloomDay2, m2, k2))
print(minDays(bloomDay3, m3, k3))
print(minDays(bloomDay4, m4, k4))
print("=" * 10)
print(minDaysBinary(bloomDay, m, k))
print(minDaysBinary(bloomDay2, m2, k2))
print(minDaysBinary(bloomDay3, m3, k3))
print(minDaysBinary(bloomDay4, m4, k4))
