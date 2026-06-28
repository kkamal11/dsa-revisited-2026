class Solution:
    def is_palindrome(self, s1):
        return s1 == s1[::-1]

    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            tmp_s = []

            for j in range(i, n):
                tmp_s.append(s[j])

                if self.is_palindrome("".join(tmp_s)):
                    count += 1

        return count

    def countSubstringsOptimised(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)  # Odd-length palindromes
            expand(i, i + 1)  # Even-length palindromes

        return count
