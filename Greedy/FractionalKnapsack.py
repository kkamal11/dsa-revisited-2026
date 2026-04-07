def knapsack_weight_val(val, wt, capacity):

    val.sort()
    wt.sort()
    n = len(val)
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
            break
    return total


val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50


print(knapsack_weight_val(val, wt, capacity))

val = [60, 100]
wt = [10, 20]
capacity = 50
print(knapsack_weight_val(val, wt, capacity))
