import math


def find_square_root(n):
    ans = 1
    for i in range(n + 1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans


def find_square_root2(n):
    if n == 1:
        return 1
    lo = 0
    hi = n // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


n1 = 1
n2 = 36
n3 = 25
n4 = 225
n5 = 226
n6 = 362
n7 = 4
n8 = 3

print(math.floor(math.sqrt(n1)), find_square_root(n1))
print(math.floor(math.sqrt(n2)), find_square_root(n2))
print(math.floor(math.sqrt(n3)), find_square_root(n3))
print(math.floor(math.sqrt(n4)), find_square_root(n4))
print(math.floor(math.sqrt(n5)), find_square_root(n5))
print(math.floor(math.sqrt(n6)), find_square_root(n6))
print(math.floor(math.sqrt(n8)), find_square_root(n8))
print(math.floor(math.sqrt(n7)), find_square_root(n7))
print("=" * 16)
print(math.floor(math.sqrt(n1)), find_square_root2(n1))
print(math.floor(math.sqrt(n2)), find_square_root2(n2))
print(math.floor(math.sqrt(n3)), find_square_root2(n3))
print(math.floor(math.sqrt(n4)), find_square_root2(n4))
print(math.floor(math.sqrt(n5)), find_square_root2(n5))
print(math.floor(math.sqrt(n6)), find_square_root2(n6))
print(math.floor(math.sqrt(n8)), find_square_root2(n8))
print(math.floor(math.sqrt(n7)), find_square_root2(n7))
