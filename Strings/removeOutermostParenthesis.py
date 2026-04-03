class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level = 0
        res = []
        for char in s:
            if char == "(":
                level += 1
            if level > 1:
                if char == "(":
                    res.append("(")
                else:
                    res.append(")")
            if char == ")":
                level -= 1

        return "".join(res)


s = "(()())(())"  # "()()()"
s2 = "(()())(())(()(()))"  # "()()()()(())"
sol = Solution()
print(sol.removeOuterParentheses(s))
print(sol.removeOuterParentheses(s2))
