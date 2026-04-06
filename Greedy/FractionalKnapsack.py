def knapsack_weight_val(val, wt, capacity):
    n = len(val)
    i = 0
    j = 0
    total = 0
    twt = 0

    for i in range(n):
        v = val[i]
        w = wt[i]
        if twt + w <= capacity:
            twt += w
            total += v
        else:
            frac = (capacity - twt)/twt
            total += frac * v
    return total


val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

print(knapsack_weight_val(val, wt, capacity))