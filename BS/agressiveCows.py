"""
You are given an array with unique elements of stalls[], which
denote the positions of stalls. You are also given an integer k
which denotes the number of aggressive cows. The task is to assign
stalls to k cows such that the minimum distance between any two of
them is the maximum possible.

Input: stalls = [1, 2, 8, 4, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[2] and
the third cow can be placed at stalls[3].
The minimum distance between cows in this case is 3, which is the largest among all possible ways.

Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[3].
The minimum distance between cows in this case is 4, which is the largest among all possible ways.
"""


def canPlace(stalls, dist, k):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls) - 1):
        if stalls[i] - last >= dist:
            count += 1
    return count >= k


def aggressive_cows(stalls, k):
    stalls.sort()
    n = stalls[-1] - stalls[0] + 1
    for dist in range(1, n):
        if not canPlace(stalls, dist, k):
            return dist - 1


# Search Space [1, max(stalls) - min(stalls)]


stall = [10, 1, 2, 7, 5]
k = 3
stall1 = [1, 2, 8, 4, 9]
k1 = 3
print(aggressive_cows(stall, k))
print(aggressive_cows(stall1, k1))
