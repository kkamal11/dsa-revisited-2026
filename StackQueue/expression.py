class ExpressionConverter:

    def precedence(self, operator: str):

        if operator == "^":
            return 3
        if operator in ["*", "/"]:
            return 2
        if operator in ["+", "-"]:
            return 1
        return -1

    def infix_to_postfix(self, exp: str):
        ans = []
        stack = []

        for ch in exp:
            if ch == " ":
                continue
            if ch.isalnum():
                ans.append(ch)
            else:
                if ch == ")":
                    while stack and stack[-1] != "(":
                        ans.append(stack.pop())
                    stack.pop()
                elif (
                    not stack
                    or self.precedence(ch) > self.precedence(stack[-1])
                    or ch == "("
                ):
                    stack.append(ch)
                else:
                    while stack and self.precedence(stack[-1]) >= self.precedence(ch):
                        ans.append(stack.pop())
                    stack.append(ch)

        while stack:
            ans.append(stack.pop())

        return "".join(ans)

    def infix_to_prefix(self, exp: str):
        pass


conv = ExpressionConverter()
exp1 = " a + b * (c^d - e) ^ (f + g * h) - i "
exp2 = " (p + q) * (m - n)"
exp3 = "a + b * (c ^ d - e) / a"
print(conv.infix_to_postfix(exp1))
print(conv.infix_to_postfix(exp2))
print(conv.infix_to_postfix(exp3))
