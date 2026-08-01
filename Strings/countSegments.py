class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        last = " "

        for ch in s:
            if ch == " " and last != " ":
                ans += 1
            last = ch

        if last != " ":
            ans += 1

        return ans

    def countSegments(self, s: str) -> int:
        """
        split() without arguments automatically:
            ignores leading/trailing spaces,
            treats multiple consecutive spaces as one separator.
        """

        return len(s.split())
