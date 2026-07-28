"""
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take
turns to remove 1 to 3 stones. The one who removes the last stone
will be the winner. You will take the first turn to remove the stones.
Given n, the number of stones in the heap, return true if you can win
the game


Although the problem may seem simple, it has a mathematical solution.

Approach:
1. n = 1: You can take all stones and win.
2. n = 2: You can take all stones and win.
3. n = 3: You can take all stones and win.
4. n = 4: No matter how many stones you take (1, 2, or 3), your friend can take the remaining stones and win.
5. n = 5: You can take 1 stone, leaving 4 for your friend, and win.
6. n = 6: You can take 2 stones, leaving 4 for your
    friend, and win.
7. n = 7: You can take 3 stones, leaving 4 for your friend, and win.
8. n = 8: No matter how many stones you take (1, 2, or 3), your friend can take the remaining stones and win.

Observation:
- If n is a multiple of 4, you will lose the game if your friend plays


"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
