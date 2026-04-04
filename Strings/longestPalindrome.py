class Solution:
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        start = end = 0
        for i in range(n):
            sub = ""
            for j in range(i, n):
                sub += s[j]
                if self.isPalindrome(sub):
                    if len(sub) > max_len:
                        max_len = j - i + 1
                        start = i
                        end = j
        return s[start : end + 1]

    def longestPalindromeOptimised(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start = end = 0

        for i in range(len(s)):
            # odd length
            l1, r1 = expand(i, i)
            # even length
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]


sol = Solution()
s = "babad"
s2 = "cbbd"
print(sol.longestPalindrome(s))
print(sol.longestPalindrome(s2))
