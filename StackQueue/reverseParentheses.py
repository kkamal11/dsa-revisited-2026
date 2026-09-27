class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        (ed(et(oc))el)
        (ed(etco)el)
        (edocteel)
        leetcode

        (ed(et(oc
        (ed(etco


        Complexity Analysis
        Time complexity : O(n^2). We traverse the input string once and for each closing parenthesis, we pop all the characters from the stack until we reach an opening parenthesis. In the worst case, we may have to pop all the characters from the stack for each closing parenthesis, leading to a time complexity of O(n^2).
        Space complexity : O(n). We use a stack to store the characters of the input string.
        """
        stack = []
        inner = []
        for ch in s:
            if ch == ")":
                while stack:
                    last = stack.pop()
                    if last == "(":
                        stack.extend(inner)
                        inner = []
                        break
                    inner.append(last)
            else:
                stack.append(ch)

        return "".join(stack)

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        result = []
        i = 0
        direction = 1

        while 0 <= i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction = -direction
            else:
                result.append(s[i])

            i += direction

        return "".join(result)
