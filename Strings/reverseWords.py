class Solution:

    def reverseWords(self, s: str) -> str:
        res = ""
        curr = ""
        n = len(s)

        for i in range(n - 1, -1, -1):
            curr = curr + s[i]
            if s[i] == " ":
                res = curr + res
                curr = ""

        res = curr + " " + res
        return res.strip()

    def reverseWords(self, s: str) -> str:
        res = []
        curr = []
        n = len(s)

        for i in range(n - 1, -1, -1):
            curr.append(s[i])
            if s[i] == " ":
                res.append("".join(curr))
                curr = []

        res.append("".join(curr))

        return " ".join((c.strip() for c in reversed(res)))

    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        start = 0
        while start < n:
            end = start
            while end < n and chars[end] != " ":
                end += 1

            l, r = start, end - 1
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

            start = end + 1

        return "".join(chars)
