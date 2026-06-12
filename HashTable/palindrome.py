"""
Given a string s, return the length of the longest palindrome that
can be built with those letters.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = 0
        mapp = {}
        odd_found = False

        for i in range(len(s)):
            mapp[s[i]] = mapp.get(s[i], 0) + 1

        for k, v in mapp.items():
            if v % 2 == 0:
                max_len += v
            else:
                max_len += v - 1
                odd_found = True

        if odd_found:
            max_len += 1

        return max_len
