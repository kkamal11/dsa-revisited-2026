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
