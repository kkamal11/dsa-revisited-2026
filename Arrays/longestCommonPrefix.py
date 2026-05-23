"""
Given two arrays of integers, find the length of the longest common prefix
between any two integers, one from each array.
Example 1:
Input: arr1 = [123, 456, 789], arr2 = [12, 45, 78]
Output: 2
Explanation: The longest common prefix is "12" between 123 and 12,
which has a length of 2.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def long_prefix(s1, s2):

            j = 0
            while j < len(s1) and j < len(s2) and s1[j] == s2[j]:
                j += 1
            return s1[:j] if j else ""

        combo = []
        for a1 in arr1:
            for a2 in arr2:
                combo.append((a1, a2))

        prefix = ""
        for a1, a2 in combo:
            p = long_prefix(str(a1), str(a2))
            if len(p) > len(prefix):
                prefix = p

        return len(prefix)

    def longestCommonPrefixOptimized(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        ans = 0

        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                pre = s[:i]
                if pre in prefixes:
                    ans = max(ans, len(pre))

        return ans
