import math

"""
Binary search can b eimplemented anywhere where we have a search space
like an array, a range of numbers from 1 and n
"""


def mutply_n_times(num, n):
    ans = 1
    for _ in range(1, n + 1):
        ans *= num
    return ans


def nth_root(num, n):
    lo = 1
    hi = num
    ans = 1
    eps = 1e-6
    while (hi - lo) > eps:
        mid = (lo + hi) / 2
        if mutply_n_times(mid, n) <= num:
            ans = mid
            lo = mid
        else:
            hi = mid
    print(f"{hi=} {lo=} {mid=}")
    return hi


num = 25
n = 2
num2 = 68
n = 2
print(math.sqrt(num), nth_root(num, n))
print(math.sqrt(num2), nth_root(num2, n))
