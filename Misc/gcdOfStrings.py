"""
Mathematical approach to find the greatest common divisor (GCD) of two strings.
The GCD of two strings is the largest string that can be concatenated
multiple times to form both strings. If no such string exists, return an empty string.

The GCD can be found using the Euclidean algorithm, which is a well-known method for
finding the GCD of two integers. The same principle can be applied to strings by checking if the concatenation of the two strings in different orders is equal.
If they are not equal, it means there is no common divisor string.
If they are equal, we can find the GCD of the lengths of the two strings
and return the substring of that length from either string.
The time complexity of this approach is O(n + m), where n and m are the lengths
of the two strings.
The space complexity is O(1) since we are only using a constant amount of extra space.


If two strings are made by repeating the same base string, then concatenating them in either order produces the same result.
"""


class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = self.gcd(len(str1), len(str2))

        return str1[:length]
