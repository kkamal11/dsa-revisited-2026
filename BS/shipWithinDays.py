# weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def canShipInDay(weights, days, capacity):
    loaded_weight = 0
    days_req = 1
    """Day 1 nothing is loaded"""
    for w in weights:
        loaded_weight += w
        if loaded_weight > capacity:
            days_req += 1
            loaded_weight = w

    return days_req <= days


def shipWithinDays(weights, days):
    capacity_min = max(weights)
    capacity_max = sum(weights)
    for capacity in range(capacity_min, capacity_max + 1):
        if canShipInDay(weights, days, capacity):
            return capacity


def shipWithinDaysBinary(weights, days):
    lo = max(weights)
    hi = sum(weights)
    ans = -1
    while lo <= hi:
        cap_req = (lo + hi) // 2
        if canShipInDay(weights, days, cap_req):
            ans = cap_req
            hi = cap_req - 1
        else:
            lo = cap_req + 1
    return ans


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

weights2 = [3, 2, 2, 4, 1, 4]
days2 = 3

weights4 = [1, 2, 3, 1, 1]
days4 = 4

weights5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days5 = 1
print(shipWithinDays(weights, days))
print(shipWithinDays(weights2, days2))
print(shipWithinDays(weights4, days4))
print(shipWithinDays(weights5, days5))
print("=" * 10)
print(shipWithinDaysBinary(weights, days))
print(shipWithinDaysBinary(weights2, days2))
print(shipWithinDaysBinary(weights4, days4))
print(shipWithinDaysBinary(weights5, days5))
