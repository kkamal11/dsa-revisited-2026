def is_ith_bit_set(n, i):
    return (n & (1 << i)) != 0


n = 10
i = 1
print(is_ith_bit_set(n, i))
print(is_ith_bit_set(n, 2))
