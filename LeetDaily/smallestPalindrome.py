from itertools import permutations
from typing import Optional
from collections import Counter


class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def smallestPalindrome(self, s: str) -> Optional[str]:
        p = permutations(s)
        s_list = ["".join(list(pp)) for pp in p]
        s_list.sort()
        for s in s_list:
            if self.is_palindrome(s):
                return s
        return None

    def smallestPalindrome2(self, s: str) -> Optional[str]:

        count = Counter(s)

        half = []
        middle = ""
        for char, freq in sorted(count.items()):
            half.append(char * (freq // 2))
            if freq % 2 == 1:
                middle = char

        half_str = "".join(half)
        return half_str + middle + half_str[::-1]
